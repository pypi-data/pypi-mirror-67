
import datetime as dt
from collections import defaultdict, Counter
from collections.abc import Mapping, Sequence
from logging import getLogger
from re import compile

import numpy as np
import pandas as pd
from sqlalchemy import inspect, select, and_, or_, distinct, asc, desc
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.functions import coalesce

from .coasting import CoastingBookmark
from ..lib.data import kargs_to_attr
from ..lib.date import local_time_to_time, time_to_local_time, YMD, HMS, to_date, local_date_to_time
from ..sql import StatisticName, StatisticJournal, StatisticJournalInteger, ActivityJournal, \
    StatisticJournalFloat, StatisticJournalText, Interval, StatisticMeasure, Source
from ..sql.database import connect, ActivityTimespan, ActivityGroup, ActivityBookmark, StatisticJournalType, \
    Composite, CompositeComponent, ActivityNearby
from ..names import DELTA_TIME, HEART_RATE, _src, FITNESS_D_ANY, FATIGUE_D_ANY, like, HEART_RATE_BPM, \
    MED_HEART_RATE_BPM, GRADE, GRADE_PC, BOOKMARK, DISTANCE_KM, MED_SPEED_KMH, MED_HR_IMPULSE_10, MED_CADENCE, \
    ELEVATION_M, CLIMB_MS, ACTIVE_TIME_H, ACTIVE_DISTANCE_KM, MED_POWER_ESTIMATE_W, TIMESPAN_ID, LATITUDE, LONGITUDE, \
    SPHERICAL_MERCATOR_X, SPHERICAL_MERCATOR_Y, DISTANCE, MED_WINDOW, ELEVATION, SPEED, HR_ZONE, HR_IMPULSE_10, \
    ALTITUDE, CADENCE, TIME, LOCAL_TIME, REST_HR, DAILY_STEPS, ACTIVE_TIME, ACTIVE_DISTANCE, POWER_ESTIMATE, INDEX, \
    GROUP, MIXED, LO_REST_HR, HI_REST_HR, _delta, FATIGUE, FITNESS

log = getLogger(__name__)


# in general these functions should (or are being written to) take both ORM objects and parameters
# to retrieve those objects if missing.  so, for example, activity_statistics can be called with
# StatisticName and ActivityJournal instances, or it can be called with more low-level parameters.
# the low-level parameters are often useful interactively but make simplifying assumptions; the ORM
# instances give complete control.


def df(query):
    # https://stackoverflow.com/questions/29525808/sqlalchemy-orm-conversion-to-pandas-dataframe
    return pd.read_sql(query.statement, query.session.bind)


def session(*args):
    ns, db = connect(args)
    return db.session()


def _add_constraint(q, attribute, value, key):
    if value is not None:
        if isinstance(value, Mapping):
            if key in value:
                q = q.filter(attribute == value[key])
        elif isinstance(value, str):
            q = q.filter(attribute == value)
        elif isinstance(value, Sequence):
            q = q.filter(attribute.in_(value))
        else:
            q = q.filter(attribute == value)
    return q


def _collect_statistics(s, names, owner=None, activity_group=None):
    if not names:
        names = ['%']
    statistic_ids, statistic_names = set(), set()
    for name in names:
        q = s.query(StatisticName).filter(StatisticName.name.like(name))
        q = _add_constraint(q, StatisticName.owner, owner, name)
        q = _add_constraint(q, StatisticName.activity_group, ActivityGroup.from_name(s, activity_group), name)
        for statistic_name in q.all():
            statistic_ids.add(statistic_name.id)
            statistic_names.add(statistic_name.name)
    return statistic_names, statistic_ids


def _tables():
    return kargs_to_attr(sj=inspect(StatisticJournal).local_table,
                         sn=inspect(StatisticName).local_table,
                         sji=inspect(StatisticJournalInteger).local_table,
                         sjf=inspect(StatisticJournalFloat).local_table,
                         sjt=inspect(StatisticJournalText).local_table,
                         inv=inspect(Interval).local_table,
                         at=inspect(ActivityTimespan).local_table,
                         aj=inspect(ActivityJournal).local_table,
                         cmp=inspect(Composite).local_table,
                         cc=inspect(CompositeComponent).local_table,
                         src=inspect(Source).local_table)


def _build_statistic_journal_query(statistic_ids, start, finish, source_ids, schedule):

    # use more efficient expression interface and exploit the fact that
    # alternative journal types will be null in an outer join.

    t = _tables()

    q = select([t.sn.c.name, t.sj.c.time, coalesce(t.sjf.c.value, t.sji.c.value, t.sjt.c.value)]). \
        select_from(t.sj.join(t.sn).outerjoin(t.sjf).outerjoin(t.sji).outerjoin(t.sjt)). \
        where(t.sn.c.id.in_(statistic_ids))
    if start:
        q = q.where(t.sj.c.time >= start)
    if finish:
        q = q.where(t.sj.c.time <= finish)
    if source_ids is not None:  # avoid testing DataFrame sequences as bools
        # int() to convert numpy types
        q = q.where(t.sj.c.source_id.in_(int(id) for id in source_ids))
    if schedule:
        q = q.join(t.inv).where(t.inv.c.schedule == schedule)
    q = q.order_by(t.sj.c.time)
    return q


class MissingData(Exception): pass


def make_pad(data, times, statistic_names, quiet=False):
    err_cnt = defaultdict(lambda: 0)

    def pad():
        nonlocal data, times
        n = len(times)
        for name in statistic_names:
            if len(data[name]) != n:
                err_cnt[name] += 1
                if err_cnt[name] <= 1 and not quiet:
                    log.warning('Missing %s at %s (single warning)' % (name, times[-1]))
                data[name].append(None)

    return pad


def activity_journal(s, activity_journal=None, local_time=None, time=None, activity_group=None):
    if activity_journal:
        if local_time or time or activity_group:
            raise Exception('Activity Journal given, so extra activity-related parameters are unused')
    else:
        if local_time:
            time = local_time_to_time(local_time)
        if not time:
            raise Exception('Specify activity_journal or time')
        try:
            # first, if an activity includes that time
            q = s.query(ActivityJournal). \
                filter(ActivityJournal.start <= time,
                       ActivityJournal.finish >= time)
            if activity_group:
                q = q.filter(ActivityJournal.activity_group == ActivityGroup.from_name(s, activity_group))
            activity_journal = q.one()
        except NoResultFound:
            # second, if anything in the following 24 hours (eg if just date given)
            q = s.query(ActivityJournal). \
                filter(ActivityJournal.start > time,
                       ActivityJournal.finish < time + dt.timedelta(days=1))
            if activity_group:
                q = q.filter(ActivityJournal.activity_group == ActivityGroup.from_name(s, activity_group))
            activity_journal = q.one()
        log.info(f'Using Activity Journal {activity_journal}')
    return activity_journal

_activity_journal = activity_journal


def _add_bookmark(bookmark, df):
    df[BOOKMARK] = bookmark.id
    return df


def activity_statistics(s, *statistics, start=None, finish=None, owner=None, bookmark_constraint=None,
                        local_time=None, time=None, bookmarks=None, activity_journal=None,
                        activity_group=None, with_timespan=False, check=True):

    if bookmarks:
        if start or finish or local_time or time or activity_journal or activity_group:
            raise Exception('Cannot use bookmarks with additional activity constraints')
        return pd.concat(_add_bookmark(bookmark,
                                       _activity_statistics(s, *statistics, owner=owner,
                                                            bookmark_constraint=bookmark_constraint,
                                                            start=bookmark.start, finish=bookmark.finish,
                                                            activity_journal=bookmark.activity_journal,
                                                            with_timespan=with_timespan, check=check))
                         for bookmark in bookmarks)
    else:
        return _activity_statistics(s, *statistics, owner=owner, bookmark_constraint=bookmark_constraint,
                                    start=start, finish=finish,
                                    local_time=local_time, time=time, activity_journal=activity_journal,
                                    activity_group=activity_group, with_timespan=with_timespan, check=check)


def _activity_statistics(s, *statistics, owner=None, bookmark_constraint=None, start=None, finish=None,
                         local_time=None, time=None, activity_journal=None,
                         activity_group=None, with_timespan=False, check=True):

    activity_journal = _activity_journal(s, activity_journal=activity_journal, local_time=local_time,
                                         time=time, activity_group=activity_group)
    if activity_group is None:
        activity_group = activity_journal.activity_group
    names = statistic_names(s, *statistics, owner=owner, activity_group=activity_group, check=check)
    counts = Counter(name.name for name in names)

    t = _tables()
    ttj = _type_to_journal(t)
    labels = [name.name if counts[name.name] == 1 else f'{name.name}:{name.activity_group}' for name in names]
    tables = [ttj[name.statistic_journal_type] for name in names]
    time_select = select([distinct(t.sj.c.time).label("time")]).select_from(t.sj). \
        where(and_(t.sj.c.statistic_name_id.in_([n.id for n in names]),
                   t.sj.c.source_id == activity_journal.id))
    if start:
        time_select = time_select.where(t.sj.c.time >= start)
    if finish:
        time_select = time_select.where(t.sj.c.time <= finish)
    time_select = time_select.order_by("time").alias("sub_time")  # order here avoids extra index
    sub_selects = [select([table.c.value, t.sj.c.time]).
                       select_from(t.sj.join(table)).
                       where(and_(t.sj.c.statistic_name_id == name.id,
                                  t.sj.c.source_id == activity_journal.id)).
                       order_by(t.sj.c.time).  # this doesn't affect plan but seems to speed up query
                       alias(f'sub_{name.name}_{name.activity_group}')
                   for name, table in zip(names, tables)]
    # don't call this TIME because even though it's moved to index it somehow blocks the later addition
    # of a TIME column (eg when plotting health statistics)
    selects = [time_select.c.time.label(INDEX)] + \
              [sub.c.value.label(label) for sub, label in zip(sub_selects, labels)]
    sources = time_select
    for sub in sub_selects:
        sources = sources.outerjoin(sub, time_select.c.time == sub.c.time)
    if with_timespan:
        selects += [t.at.c.id.label(TIMESPAN_ID)]
        sources = sources.outerjoin(t.at,
                                    and_(t.at.c.start <= time_select.c.time,
                                         t.at.c.finish > time_select.c.time,
                                         t.at.c.activity_journal_id == activity_journal.id))
    sql = select(selects).select_from(sources)
    # log.debug(sql)
    return pd.read_sql_query(sql=sql, con=s.connection(), index_col=INDEX)


def statistic_quartiles(s, *statistics, start=None, finish=None, owner=None, activity_group=None, sources=None,
                        schedule=None):

    # todo - rewrite using new approach

    statistic_names, statistic_ids = _collect_statistics(s, statistics, owner, activity_group)
    q = s.query(StatisticMeasure). \
        join(StatisticJournal, StatisticMeasure.statistic_journal_id == StatisticJournal.id). \
        join(StatisticName, StatisticJournal.statistic_name_id == StatisticName.id). \
        join(Source, StatisticJournal.source_id == Source.id). \
        filter(StatisticName.id.in_(statistic_ids)). \
        filter(StatisticMeasure.quartile != None)
    if start:
        q = q.filter(StatisticJournal.time >= start)
    if finish:
        q = q.filter(StatisticJournal.time <= finish)
    if sources is not None:
        q = q.filter(StatisticJournal.source.in_(sources))
    if schedule:
        q = q.join((Interval, StatisticMeasure.source_id == Interval.id)). \
            filter(Interval.schedule == schedule)
    log.debug(q)

    raw_data = defaultdict(lambda: defaultdict(lambda: [0] * 5))
    for measure in q.all():
        raw_data[measure.source.start][measure.statistic_journal.statistic_name.name][measure.quartile] = \
            measure.statistic_journal.value
    data, times = defaultdict(list), []
    for time in sorted(raw_data.keys()):
        times.append(time)
        sub_data = raw_data[time]
        for statistic in statistic_names:
            if statistic in sub_data:
                data[statistic].append(sub_data[statistic])
            else:
                data[statistic].append(None)

    return pd.DataFrame(data, index=times)


MIN_PERIODS = 1

def std_activity_statistics(s, local_time=None, time=None, activity_journal=None, activity_group=None,
                            with_timespan=True):

    stats = activity_statistics(s, LATITUDE, LONGITUDE, SPHERICAL_MERCATOR_X, SPHERICAL_MERCATOR_Y, DISTANCE,
                                ELEVATION, SPEED, HEART_RATE, HR_ZONE, HR_IMPULSE_10, ALTITUDE, GRADE, CADENCE,
                                POWER_ESTIMATE,
                                local_time=local_time, time=time, activity_journal=activity_journal,
                                activity_group=activity_group, with_timespan=with_timespan)

    stats.rename(columns={DISTANCE: DISTANCE_KM}, inplace=True)
    stats[MED_SPEED_KMH] = stats[SPEED].rolling(MED_WINDOW, min_periods=MIN_PERIODS).median() * 3.6
    if present(stats, CADENCE):
        stats[MED_CADENCE] = stats[CADENCE].rolling(MED_WINDOW, min_periods=MIN_PERIODS).median()
    if present(stats, HEART_RATE):
        stats.rename(columns={HEART_RATE: HEART_RATE_BPM}, inplace=True)
        stats[MED_HEART_RATE_BPM] = stats[HEART_RATE_BPM].rolling(MED_WINDOW, min_periods=MIN_PERIODS).median()
        stats[MED_HR_IMPULSE_10] = stats[HR_IMPULSE_10].rolling(MED_WINDOW, min_periods=MIN_PERIODS).median()
    if present(stats, POWER_ESTIMATE):
        stats[MED_POWER_ESTIMATE_W] = stats[POWER_ESTIMATE].rolling(MED_WINDOW, min_periods=MIN_PERIODS).median().clip(lower=0)
    if present(stats, ELEVATION):
        stats.rename(columns={ELEVATION: ELEVATION_M}, inplace=True)
        stats.rename(columns={GRADE: GRADE_PC}, inplace=True)

    if with_timespan:
        timespans = stats[TIMESPAN_ID].dropna().unique()
    if present(stats, HR_IMPULSE_10):
        stats[KEEP] = pd.notna(stats[HR_IMPULSE_10])
        stats.interpolate(method='time', inplace=True)
        stats = stats.loc[stats[KEEP] == True].drop(columns=[KEEP])
    else:
        stats = linear_resample_time(stats, dt=10, add_time=False)
    if with_timespan:
        stats = stats.loc[stats[TIMESPAN_ID].isin(timespans)]

    if present(stats, ELEVATION_M):
        stats[CLIMB_MS] = stats[ELEVATION_M].diff() * 0.1
    stats[TIME] = pd.to_datetime(stats.index)
    stats[LOCAL_TIME] = stats[TIME].apply(lambda x: time_to_local_time(x.to_pydatetime(), HMS))

    return stats


def std_health_statistics(s, *extra, start=None, finish=None):

    from ..pipeline.calculate.monitor import MonitorCalculator

    def merge_to_hour(stats, extra):
        return stats.merge(extra.reindex(stats.index, method='nearest', tolerance=dt.timedelta(minutes=30)),
                           how='outer', left_index=True, right_index=True)
    
    # avoid x statistics some time in first day
    start = start or s.query(StatisticJournal.time).filter(StatisticJournal.time >
                                                           local_date_to_time(to_date('1970-01-03'))) \
        .order_by(asc(StatisticJournal.time)).limit(1).scalar()
    finish = finish or s.query(StatisticJournal.time).order_by(desc(StatisticJournal.time)).limit(1).scalar()
    stats = pd.DataFrame(index=pd.date_range(start=start, end=finish, freq='1h'))

    stats_1 = statistics(s, FITNESS_D_ANY, FATIGUE_D_ANY, start=start, finish=finish, check=False)
    if present(stats_1, FITNESS_D_ANY, pattern=True):
        stats_1 = stats_1.resample('1h').mean()
        stats = merge_to_hour(stats, stats_1)
    stats_2 = statistics(s, LO_REST_HR, REST_HR, HI_REST_HR, start=start, finish=finish, owner=MonitorCalculator,
                         check=False)
    if present(stats_2, REST_HR):
        stats = merge_to_hour(stats, stats_2)
    stats_3 = statistics(s, DAILY_STEPS, ACTIVE_TIME, ACTIVE_DISTANCE, _delta(FITNESS_D_ANY), _delta(FATIGUE_D_ANY), *extra,
                         start=start, finish=finish)
    stats_3 = coallesce(stats_3, ACTIVE_TIME, ACTIVE_DISTANCE)
    stats_3 = coallesce_like(stats_3, _delta(FITNESS), _delta(FATIGUE))
    stats = merge_to_hour(stats, stats_3)
    stats[ACTIVE_TIME_H] = stats[ACTIVE_TIME] / 3600
    stats[ACTIVE_DISTANCE_KM] = stats[ACTIVE_DISTANCE] / 1000
    stats[TIME] = pd.to_datetime(stats.index)
    stats[LOCAL_TIME] = stats[TIME].apply(lambda x: time_to_local_time(x.to_pydatetime(), YMD))

    return stats


def nearby_activities(s, local_time=None, time=None, activity_group=None):
    from ..pipeline.display.activity.nearby import nearby_any_time
    activity_journal = _activity_journal(s, local_time=local_time, time=time,
                                         activity_group=activity_group)
    return nearby_any_time(s, activity_journal)


def bookmarks(s, constraint, owner=CoastingBookmark):
    yield from s.query(ActivityBookmark). \
        filter(ActivityBookmark.owner == owner,
               ActivityBookmark.constraint == constraint).all()


def statistic_names(s, *statistics, owner=None, activity_group=None, check=True):
    unresolved = [statistic for statistic in statistics if not isinstance(statistic, StatisticName)]
    if unresolved:
        q = s.query(StatisticName). \
            filter(or_(StatisticName.name.like(statistic) for statistic in unresolved))
        if owner:
            q = q.filter(StatisticName.owner == owner)
        if activity_group:
            q = q.filter(StatisticName.activity_group == ActivityGroup.from_name(s, activity_group))
        resolved = q.all()
    else:
        resolved = []
    some = [statistic for statistic in statistics if isinstance(statistic, StatisticName)] + resolved
    if check and not some:
        raise Exception(f'Found no statistics for {statistics} (owner {owner}; activity group {activity_group})')
    return some


def _type_to_journal(t):
    return {StatisticJournalType.INTEGER: t.sji,
            StatisticJournalType.FLOAT: t.sjf,
            StatisticJournalType.TEXT: t.sjt}


def statistics(s, *statistics, start=None, finish=None, local_start=None, local_finish=None,
               owner=None, activity_group=None, sources=None, with_sources=False, check=True):
    t = _tables()
    ttj = _type_to_journal(t)
    names = statistic_names(s, *statistics, owner=owner, activity_group=activity_group, check=check)
    counts = Counter(name.name for name in names)
    labels = [name.name if counts[name.name] == 1 else f'{name.name} : {name.activity_group}' for name in names]
    tables = [ttj[name.statistic_journal_type] for name in names]
    if local_start:
        if start: raise Exception('Provide only one of start, local_start')
        start = local_time_to_time(local_start)
    if local_finish:
        if finish: raise Exception('Provide only one of finish, local_finish')
        finish = local_time_to_time(local_finish)
    time_select = select([distinct(t.sj.c.time).label("time")]).select_from(t.sj). \
        where(t.sj.c.statistic_name_id.in_([n.id for n in names]))
    if start:
        time_select = time_select.where(t.sj.c.time >= start)
    if finish:
        time_select = time_select.where(t.sj.c.time <= finish)
    time_select = time_select.order_by("time").alias("sub_time")  # order here avoids extra index

    def sub_select(name, table):
        selects = [table.c.value, t.sj.c.time]
        if with_sources:
            selects += [t.sj.c.source_id]
        q = select(selects). \
            select_from(t.sj.join(table)). \
            where(t.sj.c.statistic_name_id == name.id)
        if sources:
            q = q.where(t.sj.c.source_id.in_(source.id for source in sources))
        # order_by doesn't affect plan but seems to speed up query
        return q.order_by(t.sj.c.time).alias(f'sub_{name.name}_{name.activity_group}')

    sub_selects = [sub_select(name, table) for name, table in zip(names, tables)]
    # don't call this TIME because even though it's moved to index it somehow blocks the later addition
    # of a TIME column (eg when plotting health statistics)
    selects = [time_select.c.time.label(INDEX)] + \
              [sub.c.value.label(label) for sub, label in zip(sub_selects, labels)]
    if with_sources:
        selects += [sub.c.source_id.label(_src(label)) for sub, label in zip(sub_selects, labels)]
    sources = time_select
    for sub in sub_selects:
        sources = sources.outerjoin(sub, time_select.c.time == sub.c.time)
    sql = select(selects).select_from(sources)
    return pd.read_sql_query(sql=sql, con=s.connection(), index_col=INDEX)


def present(df, *names, pattern=False):
    if pattern:
        if hasattr(df, 'columns'):
            for name in names:
                columns = like(name, df.columns)
                if not columns or not all(len(df[column].dropna()) for column in columns):
                    return False
            return True
        else:
            return df is not None and (len(df.dropna()) and all(like(name, [df.name]) for name in names))
    else:
        if hasattr(df, 'columns'):
            return all(name in df.columns and len(df[name].dropna()) for name in names)
        else:
            return df is not None and (len(df.dropna()) and all(df.name == name for name in names))


def median_d(df):
    return pd.Series(df.index).diff().median()


KEEP = 'keep'


def linear_resample(df, start=None, finish=None, d=None, quantise=True):
    log.debug(f'Linear resample with index {type(df.index)}, columns {df.columns}')
    d = d or median_d(df)
    start = start or df.index.min()
    finish = finish or df.index.max()
    if quantise:
        start, finish = int(start / d) * d, (1 + int(finish / d)) * d
    lin = pd.DataFrame({KEEP: True}, index=np.arange(start, finish, d))
    ldf = df.join(lin, how='outer', sort=True)
    # if this fails check for time-like columns
    ldf.interpolate(method='slinear', limit_area='inside', inplace=True)
    ldf = ldf.loc[ldf[KEEP] == True].drop(columns=[KEEP])
    return ldf


def median_dt(df):
    return pd.Series(df.index).diff().median().total_seconds()


def linear_resample_time(df, start=None, finish=None, dt=None, with_timespan=False, keep_nan=True, add_time=True):
    log.debug(f'Linear resample with index {type(df.index)}, columns {df.columns}')
    if with_timespan is None: with_timespan = TIMESPAN_ID in df.columns
    dt = dt or median_dt(df)
    start = start or df.index.min()
    finish = finish or df.index.max()
    lin = pd.DataFrame({KEEP: True}, index=pd.date_range(start=start, end=finish, freq=f'{dt}S'))
    ldf = df.join(lin, how='outer', sort=True)
    # if this fails check for time-like columns
    ldf.interpolate(method='index', limit_area='inside', inplace=True)
    ldf = ldf.loc[ldf[KEEP] == True].drop(columns=[KEEP])
    if add_time:
        ldf[TIME] = ldf.index
        ldf[DELTA_TIME] = ldf[TIME].diff()
    if with_timespan:
        if keep_nan:
            ldf.loc[~ldf[TIMESPAN_ID].isin(df[TIMESPAN_ID].unique())] = np.nan
        else:
            ldf = ldf.loc[ldf[TIMESPAN_ID].isin(df[TIMESPAN_ID].unique())]
    return ldf


def groups_by_time(s, start=None, finish=None):
    q = s.query(ActivityJournal.start.label(INDEX), ActivityNearby.group.label(GROUP)). \
        filter(ActivityNearby.activity_journal_id == ActivityJournal.id)
    if start:
        q = q.filter(ActivityJournal.start >= start)
    if finish:
        q = q.filter(ActivityJournal.start < finish)
    return pd.read_sql_query(sql=q.statement, con=s.connection(), index_col=INDEX)


def coallesce(df, *statistics, activity_group_label=None, mixed=MIXED,
              unpack=r'({statistic})\s*:\s*([^:]+)', pack='{statistic} : {activity_group}'):
    '''
    Combine statistics with more than one constraint.

    When multiple statistics with the same name are requested, they are distinguished by their constraint.
    This is often the activity group.  So if you request 'Active Time' for multiple groups you will get
    'Active Time (Ride)' etc.

    This function combines these into a single column (in the example, 'Active Time'), while also optionally
    extracting the constraint into a separate column.

    If two values occur at the same time they are added together.  The label is then changed to MIXED.
    '''
    for statistic in statistics:
        if activity_group_label and activity_group_label not in df.columns:
            df[activity_group_label] = np.nan
        for full_statistic, activity_group in related_statistics(df, statistic, unpack=unpack):
            if full_statistic not in df.columns:
                df[full_statistic] = np.nan
            column = pack.format(statistic=full_statistic, activity_group=activity_group)
            if activity_group_label:
                df.loc[~df[column].isna() & ~df[activity_group_label].isna() & ~(df[activity_group_label] == activity_group),
                       activity_group_label] = mixed
                df.loc[~df[column].isna() & df[activity_group_label].isna(), activity_group_label] = activity_group
            df.loc[~df[full_statistic].isna() & ~df[column].isna(), full_statistic] += \
                df.loc[~df[full_statistic].isna() & ~df[column].isna(), column]
            df.loc[df[full_statistic].isna() & ~df[column].isna(), full_statistic] = \
                df.loc[df[full_statistic].isna() & ~df[column].isna(), column]
    return df


def coallesce_like(df, *statistics):
    return coallesce(df, *statistics, unpack=r'({statistic}.*?)\s*:\s*([^:]+)')


def related_statistics(df, statistic, unpack=r'({statistic})\s*:\s*([^:]+)'):
    rx = compile(unpack.format(statistic=statistic))
    for column in df.columns:
        m = rx.match(column)
        if m: yield m.group(1), m.group(2)


def transform(df, transformation):
    transformation = {key: value for key, value in transformation.items() if key in df.columns}
    return df.transform(transformation)


def drop_empty(df):
    for column in df.columns:
        if df[column].dropna().empty:
            df = df.drop(columns=[column])
    return df


if __name__ == '__main__':
    s = session('-v5')
    # activity = std_activity_statistics(s, local_time='2018-08-03 11:52:13', activity_group='Bike')
    # print(activity.describe())
    health = std_health_statistics(s)
    print(health.describe())
