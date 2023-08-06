
from logging import getLogger
from random import choice

from sqlalchemy import func, inspect, and_, select
from sqlalchemy.sql.functions import coalesce

from .calculate import MultiProcCalculator, IntervalCalculatorMixin
from ...names import MAX, MIN, SUM, CNT, AVG, MSR
from ...lib.date import local_date_to_time
from ...sql.tables.source import Interval
from ...sql.tables.statistic import StatisticJournal, StatisticName, StatisticMeasure, StatisticJournalInteger, \
    StatisticJournalFloat, StatisticJournalText, TYPE_TO_JOURNAL_CLASS

log = getLogger(__name__)


def fuzz(n, q):
    # n is number of points, q is quartile (0-4).
    # return index for quartile that is unbiased when location not exact
    i = (n-1) * q / 4
    if i != int(i):
        i = int(i) + choice([0, 1])  # if we're between two points, pick either
    return int(i)


class SummaryCalculator(IntervalCalculatorMixin, MultiProcCalculator):

    def __init__(self, *args, owner_in='[unused]', **kargs):
        super().__init__(*args, owner_in=owner_in, **kargs)

    def _startup(self, s):
        Interval.clean(s)

    def _read_data(self, s, interval):
        # here, data is only statistics names, because calculation also involves loading data
        start, finish = local_date_to_time(interval.start), local_date_to_time(interval.finish)
        statistics_with_data_and_summary = s.query(StatisticName.id). \
            join(StatisticJournal). \
            filter(StatisticJournal.time >= start,
                   StatisticJournal.time < finish,
                   StatisticName.summary != None)
        # avoid duplicates
        return s.query(StatisticName). \
            filter(StatisticName.id.in_(statistics_with_data_and_summary)).all()

    def _calculate_results(self, s, interval, data, loader):
        start, finish = local_date_to_time(interval.start), local_date_to_time(interval.finish)
        measures = []
        for statistic_name in data:
            summaries = statistic_name.summaries
            for summary in summaries:
                value, units = self._calculate_value(s, statistic_name, summary, MIN in summaries,
                                                     start, finish, interval, measures)
                if value is not None:
                    name = self.fmt_name(statistic_name.name, summary, self.schedule)
                    # we need to infer the type
                    if summary in (MAX, MIN, SUM):
                        new_type = TYPE_TO_JOURNAL_CLASS[type(value)]
                    elif summary in (AVG,):
                        new_type = StatisticJournalFloat
                    else:
                        new_type = StatisticJournalInteger
                    loader.add(name, units, None, statistic_name.activity_group, interval, value, start, new_type,
                               description=self._describe(statistic_name, summary, interval))
        # add and commit these here - what else can we do?
        log.debug(f'Adding {len(measures)} measures')
        for measure in measures:
            s.add(measure)
        s.commit()

    def _calculate_value(self, s, statistic_name, summary, order_asc, start_time, finish_time, interval, measures):

        sj = inspect(StatisticJournal).local_table
        sji = inspect(StatisticJournalInteger).local_table
        sjf = inspect(StatisticJournalFloat).local_table
        sjt = inspect(StatisticJournalText).local_table

        units = statistic_name.units
        values = coalesce(sjf.c.value, sji.c.value, sjt.c.value)

        if summary == MAX:
            result = func.max(values)
        elif summary == MIN:
            result = func.min(values)
        elif summary == SUM:
            result = func.sum(values)
        elif summary == CNT:
            result = func.count(values)
            units = None
        elif summary == AVG:
            result = func.avg(values)
        elif summary == MSR:
            self._calculate_measures(s, statistic_name, order_asc, start_time, finish_time, interval, measures)
            return None, None
        else:
            raise Exception('Bad summary: %s' % summary)

        stmt = select([result]). \
            select_from(sj.outerjoin(sjf).outerjoin(sji).outerjoin(sjt)). \
            where(and_(sj.c.statistic_name_id == statistic_name.id,
                       sj.c.time >= start_time,
                       sj.c.time < finish_time))

        return next(s.connection().execute(stmt))[0], units

    def _describe(self, statistic_name, summary, interval):
        adjective = {MAX: 'highest', MIN: 'lowest', SUM: 'total', CNT: 'number of', AVG: 'average'}[summary]
        period = interval.schedule.describe().lower()
        if period == 'all':
            period = period + ' time'
        else:
            period = 'one ' + period
        return f'The {adjective} {statistic_name.name} over {period}.'

    def _calculate_measures(self, s, statistic_name, order_asc, start_time, finish_time, interval, measures):

        data = sorted([x for x in
                       s.query(StatisticJournal).
                           filter(StatisticJournal.statistic_name == statistic_name,
                                 StatisticJournal.time >= start_time,
                                 StatisticJournal.time < finish_time).all()
                       if x is not None and x.value is not None],
                      key=lambda x: x.value, reverse=not order_asc)

        n, local_measures = len(data), []
        for rank, journal in enumerate(data, start=1):
            if n > 1:
                percentile = (n - rank) / (n - 1) * 100
            else:
                percentile = 100
            measure = StatisticMeasure(statistic_journal=journal, source=interval, rank=rank, percentile=percentile)
            local_measures.append(measure)
            measures.append(measure)
        if n > 8:  # avoid overlap in fuzzing (and also, plot individual points in this case)
            for q in range(5):
                local_measures[fuzz(n, q)].quartile = q
        log.debug('Ranked %s' % statistic_name)

    @classmethod
    def parse_name(cls, name):
        left, right = name.split(' ', 1)
        summary, period = left.split('/')
        return summary, period, right

    @classmethod
    def fmt_name(cls, name, summary, schedule):
        title = summary[1:-1].capitalize()   # see parse_name
        return '%s/%s %s' % (title, schedule.describe(), name)
