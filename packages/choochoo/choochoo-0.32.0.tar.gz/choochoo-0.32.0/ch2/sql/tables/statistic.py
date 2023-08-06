
import datetime as dt
from enum import IntEnum
from logging import getLogger
from re import split

from sqlalchemy import Column, Integer, ForeignKey, Text, UniqueConstraint, Float, desc, asc, Index
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import relationship, backref, synonym
from sqlalchemy.orm.exc import NoResultFound

from .source import Interval
from ..support import Base
from ..types import Time, ShortCls
from ..utils import add
from ...names import KMH, PC, BPM, STEPS_UNITS, S, M, KG, W, KCAL, KJ, FF, KM, ALL
from ...diary.model import TYPE, MEASURES, SCHEDULES
from ...lib.date import format_seconds, local_date_to_time, time_to_local_time
from ...lib.utils import sigfig

log = getLogger(__name__)


class StatisticName(Base):

    __tablename__ = 'statistic_name'

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, index=True)  # simple, displayable name
    description = Column(Text)
    units = Column(Text)
    summary = Column(Text)  # '[max]', '[min]' etc - can be multiple values but each in square brackets
    owner = Column(ShortCls, nullable=False, index=True)  # index for deletion
    activity_group_id = Column(Integer, ForeignKey('activity_group.id', ondelete='cascade'), nullable=False)
    activity_group = relationship('ActivityGroup')
    statistic_journal_type = Column(Integer, nullable=False)  # StatisticJournalType
    UniqueConstraint(name, owner, activity_group_id)

    def __str__(self):
        return '%s : %s (%s)' % (self.name, self.activity_group.name if self.activity_group else None, self.owner)

    @property
    def summaries(self):
        if self.summary:
            return [x.lower() for x in split(r'[\s,]*(\[[^\]]+\])[\s ]*', self.summary) if x]
        else:
            return []

    @classmethod
    def add_if_missing(cls, s, name, type, units, summary, owner, activity_group=ALL, description=None):
        from .activity import ActivityGroup
        activity_group = ActivityGroup.from_name(s, activity_group)
        s.commit()  # start new transaction here in case rollback
        q = s.query(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group)  # allows instances
        statistic_name = q.one_or_none()
        if not statistic_name:
            statistic_name = add(s, StatisticName(name=name, units=units, summary=summary, owner=owner,
                                                  activity_group=activity_group, statistic_journal_type=type,
                                                  description=description))
            try:
                s.flush()
            except IntegrityError as e:  # worker may have created in parallel, so read
                log.debug(f'Rollback for {e}')
                s.rollback()
                log.debug('Now trying retrieval...')
                statistic_name = q.one()
                log.debug('Retrieved')
        else:
            if statistic_name.statistic_journal_type != type:
                raise Exception('Changing type on %s (%s -> %s)' %
                                (statistic_name.name, statistic_name.statistic_journal_type, type))
            if statistic_name.units != units:
                log.warning('Changing units on %s (%s -> %s)' % (statistic_name.name, statistic_name.units, units))
                statistic_name.units = units
                s.flush()
            if statistic_name.summary != summary:
                log.warning('Changing summary on %s (%s -> %s)' % (statistic_name.name, statistic_name.summary, summary))
                statistic_name.summary = summary
                s.flush()
            if statistic_name.description != description:
                log.warning('Changing description on %s (%s -> %s)' % (statistic_name.name, statistic_name.description, description))
                statistic_name.description = description
                s.flush()
        return statistic_name

    @classmethod
    def from_name(cls, s, name, owner, activity_group=ALL):
        from .activity import ActivityGroup
        return s.query(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == ActivityGroup.from_name(s, activity_group)).one()

    @classmethod
    def parse(cls, name, default_owner=None, default_activity_group=None):
        # TODO - no longer have None
        '''
        This parses the standard, extended format for naming statistics.  It is one to three fields, separated by ':'.
        These are one of 'name', 'owner:name', or 'owner:name:activity_group'.
        Currently this is used only by reftuple which itself is used only in the power pipeline configuration.
        '''
        parts, owner, activity_group = name.split(':'), None, None
        if len(parts) == 1:
            name = parts[0]
        elif len(parts) == 2:
            owner, name = parts
        else:
            owner, name, activity_group = parts
        if not owner: owner = default_owner
        if not owner:
            raise Exception(f'Missing owner for {name}')
        if not activity_group: activity_group = default_activity_group
        if activity_group == 'None': activity_group = None
        return owner, name, activity_group


class StatisticJournalType(IntEnum):

    STATISTIC = 0
    INTEGER = 1
    FLOAT = 2
    TEXT = 3
    TIMESTAMP = 4


class StatisticJournal(Base):

    __tablename__ = 'statistic_journal'

    id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False, index=True)  # index needed for fast delete of subtypes
    statistic_name_id = Column(Integer, ForeignKey('statistic_name.id', ondelete='cascade'),
                               nullable=False, index=True)
    statistic_name = relationship('StatisticName')
    source_id = Column(Integer, ForeignKey('source.id', ondelete='cascade'),
                       nullable=False, index=True)
    source = relationship('Source')
    time = Column(Time, nullable=False)
    # serial "counts" along values in the timeseries.  it's optional.  for garmin, all values appear each
    # record, so all imported values share the same serial.  but that's not true for the corrected elevation,
    # for example.
    serial = Column(Integer)
    # relax this for kit support (add source_id)
    UniqueConstraint(statistic_name_id, time, source_id)
    UniqueConstraint(serial, source_id, statistic_name_id)
    Index('from_activity_timespan', source_id, statistic_name_id, time)  # time last since inequality

    __mapper_args__ = {
        'polymorphic_identity': StatisticJournalType.STATISTIC,
        'polymorphic_on': 'type'
    }

    def __str__(self):
        try:
            return 'StatisticJournal "%s"' % self.value
        except AttributeError:
            return 'StatisticJournal base'

    @classmethod
    def add(cls, s, name, units, summary, owner, activity_group, source, value, time, serial, type,
            description=None):
        statistic_name = StatisticName.add_if_missing(s, name, type, units, summary, owner,
                                                      activity_group=activity_group, description=description)
        journal = STATISTIC_JOURNAL_CLASSES[type](statistic_name=statistic_name, source=source,
                                                  value=value, time=time, serial=serial)
        s.add(journal)
        return journal

    def formatted(self):
        if self.value is None:
            return None
        units = self.statistic_name.units
        if not units:
            return '%d' % self.value
        elif units == M:
            if self.value > 2000:
                return '%d km' % (self.value / 1000)
            else:
                return '%d m' % self.value
        elif units == S:
            return format_seconds(self.value)
        elif units in (KMH, PC, BPM, STEPS_UNITS, W, KJ):
            return '%d %s' % (self.value, units)
        elif units == KCAL:
            return '%s %s' % (sigfig(self.value, 2), units)
        else:
            return '%d %s' % (self.value, units)

    def measures_as_text(self, date):
        words = []
        if hasattr(self, 'measures'):
            for measure in sorted(self.measures,
                                  key=lambda measure: measure.source.schedule.frame_length_in_days(date)):
                if words:
                    words += [',']
                quintile = 1 + min(4, measure.percentile / 20)
                words += [('quintile-%d' % quintile, '%d%%' % int(measure.percentile))]
                if measure.rank < 5:
                    words += [':', ('rank-%d' % measure.rank, '%d' % measure.rank)]
                words += ['/' + measure.source.schedule.describe(compact=True)]
        return words

    def measures_as_model(self, date):
        if hasattr(self, 'measures'):
            measures = {TYPE: MEASURES, SCHEDULES: {}}
            for measure in sorted(self.measures,
                                  key=lambda measure: measure.source.schedule.frame_length_in_days(date),
                                  reverse=True):
                measures[SCHEDULES][measure.source.schedule.describe(compact=True)] = (measure.percentile, measure.rank)
            return measures
        else:
            return None

    @classmethod
    def at_date(cls, s, date, name, owner, activity_group, source_id=None):
        start = local_date_to_time(date)
        finish = start + dt.timedelta(days=1)
        q = s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticJournal.time >= start,
                   StatisticJournal.time < finish,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group)
        if source_id is not None:
            q = q.filter(StatisticJournal.source_id == source_id)
        return q.one_or_none()

    @classmethod
    def at(cls, s, time, name, owner, activity_group):
        return s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticJournal.time == time,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group).one_or_none()

    @classmethod
    def at_like(cls, s, time, name, owner, activity_group):
        return s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name.like(name),
                   StatisticJournal.time == time,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group).all()

    @classmethod
    def before(cls, s, time, name, owner, activity_group):
        return s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticJournal.time <= time,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group). \
            order_by(desc(StatisticJournal.time)).limit(1).one_or_none()

    @classmethod
    def before_not_null(cls, s, time, name, owner, activity_group):
        try:
            statistic_name = s.query(StatisticName). \
                filter(StatisticName.name == name,
                       StatisticName.owner == owner,
                       StatisticName.activity_group == activity_group).one()
        except NoResultFound:
            raise Exception(f'The statistic name "{name}" (owner {owner}, activity_group {activity_group}) '
                            'is undefined in the database')
        journal = STATISTIC_JOURNAL_CLASSES[statistic_name.statistic_journal_type]
        return s.query(journal). \
            filter(journal.statistic_name == statistic_name,
                   journal.time <= time,
                   journal.value != None). \
            order_by(desc(journal.time)).limit(1).one_or_none()

    @classmethod
    def after(cls, s, time, name, owner, activity_group):
        return s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticJournal.time >= time,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group). \
            order_by(asc(StatisticJournal.time)).limit(1).one_or_none()

    @classmethod
    def at_interval(cls, s, start, schedule, statistic_owner, statistic_group, interval_owner):
        return s.query(StatisticJournal).join(StatisticName, Interval). \
                    filter(StatisticJournal.statistic_name_id == StatisticName.id,
                           Interval.schedule == schedule,
                           Interval.start == start,
                           Interval.owner == interval_owner,
                           StatisticName.owner == statistic_owner,
                           StatisticName.activity_group == statistic_group). \
                    order_by(StatisticName.activity_group_id,  # order places summary stats from same source together
                             StatisticName.name).all()

    @classmethod
    def for_source(cls, s, source_id, name, owner, activity_group):
        return s.query(StatisticJournal).join(StatisticName). \
            filter(StatisticName.name == name,
                   StatisticName.owner == owner,
                   StatisticName.activity_group == activity_group,
                   StatisticJournal.source_id == source_id).one_or_none()


class StatisticJournalInteger(StatisticJournal):

    __tablename__ = 'statistic_journal_integer'

    id = Column(Integer, ForeignKey('statistic_journal.id', ondelete='cascade'), primary_key=True)
    value = Column(Integer)

    __mapper_args__ = {
        'polymorphic_identity': StatisticJournalType.INTEGER
    }

    def set(self, value):
        self.value = value if value is None else int(value)

    @classmethod
    def add(cls, s, name, units, summary, owner, activity_group, source, value, time, serial=None, description=None):
        return super().add(s, name, units, summary, owner, activity_group, source, value, time, serial,
                           StatisticJournalType.INTEGER, description=description)


class StatisticJournalFloat(StatisticJournal):

    __tablename__ = 'statistic_journal_float'

    id = Column(Integer, ForeignKey('statistic_journal.id', ondelete='cascade'), primary_key=True)
    value = Column(Float)

    def set(self, value):
        self.value = value if value is None else float(value)

    @classmethod
    def add(cls, s, name, units, summary, owner, activity_group, source, value, time, serial=None, description=None):
        return super().add(s, name, units, summary, owner, activity_group, source, value, time, serial,
                           StatisticJournalType.FLOAT, description=description)

    __mapper_args__ = {
        'polymorphic_identity': StatisticJournalType.FLOAT
    }

    def formatted(self):
        if self.value is None:
            return None
        units = self.statistic_name.units
        if not units:
            return '%f' % self.value
        elif units == M:
            if self.value > 2000:
                return '%.1f km' % (self.value / 1000)
            else:
                return '%d m' % int(self.value)
        elif units == KM:
            if self.value > 2:
                return '%.1f km' % self.value
            else:
                return '%d m' % int(self.value * 1000)
        elif units == S:
            return format_seconds(self.value)
        elif units in (KMH, PC, KG, W, KJ):
            return '%.1f %s' % (self.value, units)
        elif units == KCAL:
            return '%s %s' % (sigfig(self.value, 2), units)
        elif units in (BPM, STEPS_UNITS):
            return '%d %s' % (int(self.value), units)
        elif units == FF:
            return '%d' % int(self.value)
        else:
            return '%s %s' % (self.value, units)


class StatisticJournalText(StatisticJournal):

    __tablename__ = 'statistic_journal_text'

    id = Column(Integer, ForeignKey('statistic_journal.id', ondelete='cascade'), primary_key=True)
    value = Column(Text)

    def set(self, value):
        self.value = value if value is None else str(value)

    @classmethod
    def add(cls, s, name, units, summary, owner, activity_group, source, value, time, serial=None, description=None):
        return super().add(s, name, units, summary, owner, activity_group, source, value, time, serial,
                           StatisticJournalType.TEXT, description=description)

    __mapper_args__ = {
        'polymorphic_identity': StatisticJournalType.TEXT
    }

    def formatted(self):
        if self.value is None:
            return None
        units = self.statistic_name.units
        if not units:
            return '%s' % self.value
        else:
            return '%s %s' % (self.value, units)


class StatisticJournalTimestamp(StatisticJournal):

    __tablename__ = 'statistic_journal_timestamp'

    id = Column(Integer, ForeignKey('statistic_journal.id', ondelete='cascade'), primary_key=True)
    value = synonym('time')

    __mapper_args__ = {
        'polymorphic_identity': StatisticJournalType.TIMESTAMP
    }

    @classmethod
    def add(cls, s, name, units, summary, owner, activity_group, source, time, serial=None, description=None):
        statistic_name = StatisticName.add_if_missing(s, name, StatisticJournalType.TIMESTAMP,
                                                      units, summary, owner,
                                                      activity_group=activity_group, description=description)
        journal = StatisticJournalTimestamp(statistic_name=statistic_name, source=source, time=time, serial=serial)
        s.add(journal)
        return journal

    def formatted(self):
        return time_to_local_time(self.value)


class StatisticMeasure(Base):

    __tablename__ = 'statistic_measure'

    id = Column(Integer, primary_key=True)
    statistic_journal_id = Column(Integer, ForeignKey('statistic_journal.id', ondelete='cascade'),
                                  nullable=False, index=True)
    statistic_journal = relationship('StatisticJournal',
                                     backref=backref('measures', cascade='all, delete-orphan',
                                                     passive_deletes=True,
                                                     order_by='desc(StatisticMeasure.rank)'))
    source_id = Column(Integer, ForeignKey('source.id', ondelete='cascade'),
                       nullable=False, index=True)  # must be an interval
    source = relationship('Source')
    rank = Column(Integer, nullable=False)  # 1 is best [1..n]
    percentile = Column(Float, nullable=False)  # 100 is best [0..100]
    quartile = Column(Integer)  # 0..4 at the min, 25%, median, 75% and max points


STATISTIC_JOURNAL_CLASSES = {
    StatisticJournalType.INTEGER: StatisticJournalInteger,
    StatisticJournalType.FLOAT: StatisticJournalFloat,
    StatisticJournalType.TEXT: StatisticJournalText,
    StatisticJournalType.TIMESTAMP: StatisticJournalTimestamp
}

STATISTIC_JOURNAL_TYPES = {
    StatisticJournalInteger: StatisticJournalType.INTEGER,
    StatisticJournalFloat: StatisticJournalType.FLOAT,
    StatisticJournalText: StatisticJournalType.TEXT,
    StatisticJournalTimestamp: StatisticJournalType.TIMESTAMP
}

TYPE_TO_JOURNAL_CLASS = {
    int: StatisticJournalInteger,
    float: StatisticJournalFloat,
    str: StatisticJournalText,
    dt.datetime: StatisticJournalTimestamp
}
