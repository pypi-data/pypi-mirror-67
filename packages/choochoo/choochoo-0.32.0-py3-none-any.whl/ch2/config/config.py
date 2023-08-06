

from logging import getLogger

from .climb import add_climb, CLIMB_CNAME
from .database import add_loader_support, add_activity_group, add_activities, Counter, add_statistics, add_displayer, \
    name_constant, add_monitor, add_activity_constant, add_constant, add_diary_topic, add_diary_topic_field, \
    add_activity_topic_field, add_activity_displayer_delegate
from .impulse import add_impulse
from .impulse import add_responses
from ..commands.args import base_system_path, DB_VERSION, PERMANENT
from ..commands.garmin import GARMIN_USER, GARMIN_PASSWORD
from ..names import SPORT_CYCLING, SPORT_RUNNING, SPORT_SWIMMING, SPORT_WALKING, FITNESS_D, FTHR, BPM, FATIGUE_D, \
    LATITUDE, DEG, LONGITUDE, HEART_RATE, SPEED, DISTANCE, KM, MS, ALTITUDE, CADENCE, RPM, M, ALL
from ..diary.model import TYPE, EDIT, FLOAT, LO, HI, DP, SCORE
from ..lib.schedule import Schedule
from ..pipeline.calculate.achievement import AchievementCalculator
from ..pipeline.calculate.activity import ActivityCalculator
from ..pipeline.calculate.elevation import ElevationCalculator
from ..pipeline.calculate.kit import KitCalculator
from ..pipeline.calculate.monitor import MonitorCalculator
from ..pipeline.calculate.response import ResponseCalculator
from ..pipeline.calculate.segment import SegmentCalculator
from ..pipeline.calculate.summary import SummaryCalculator
from ..pipeline.display.activity.activity import ActivityDisplayer, ActivityDelegate
from ..pipeline.display.activity.achievement import AchievementDelegate
from ..pipeline.display.activity.jupyter import JupyterDelegate
from ..pipeline.display.activity.nearby import NearbyDelegate
from ..pipeline.display.activity.segment import SegmentDelegate
from ..pipeline.display.database import DatabaseDisplayer
from ..pipeline.display.diary import DiaryDisplayer
from ..pipeline.display.monitor import MonitorDisplayer
from ..pipeline.display.response import ResponseDisplayer
from ..pipeline.read.monitor import MonitorReader
from ..pipeline.read.segment import SegmentReader
from ..sql import DiaryTopicJournal, StatisticJournalType, ActivityTopicField, SystemConstant
from ..sql.types import short_cls, long_cls
from ..srtm.file import SRTM1_DIR

log = getLogger(__name__)

NOTES = 'Notes'

BROKEN = 'broken'

BIKE = 'Bike'
RUN = 'Run'
SWIM = 'Swim'
WALK = 'Walk'


class Config:
    '''
    A class-based approach so that we can easily modify the config for different profiles.
    '''

    def __init__(self, sys, base, no_diary=False):
        self._sys = sys
        self._base = base
        self._no_diary = no_diary
        self._activity_groups = {}

    def load(self, s):
        # hopefully you won't need to over-ride this, but instead one of the more specific methods
        self._pre(s)
        self._load_activity_group(s, ALL, 'All activities')  # a widely used default
        add_loader_support(s)  # required by standard statistics calculations
        self._load_specific_activity_groups(s)
        self._load_activities_pipeline(s, Counter())
        self._load_statistics_pipeline(s, Counter())
        self._load_diary_pipeline(s, Counter())
        self._load_monitor_pipeline(s, Counter())
        self._load_constants(s)
        if not self._no_diary:
            self._load_diary_topics(s, Counter())
            self._load_activity_topics(s, Counter())
            self._post_diary(s)
        self._post(s)

    def _pre(self, s):
        self._sys.set_constant(SystemConstant.DB_VERSION, DB_VERSION + ' ' + BROKEN)

    def _post_diary(self, s):
        pass

    def _post(self, s):
        self._sys.set_constant(SystemConstant.DB_VERSION, DB_VERSION, force=True)

    def _load_specific_activity_groups(self, s):
        # statistic rankings (best of month etc) are calculated per group
        self._load_activity_group(s, BIKE, 'Cycling activities')
        self._load_activity_group(s, RUN, 'Running activities')
        self._load_activity_group(s, SWIM, 'Swimming activities')
        self._load_activity_group(s, WALK, 'Walking activities')

    def _load_activity_group(self, s, name, description):
        log.debug(f'Loading activity group {name}')
        self._activity_groups[name] = add_activity_group(s, name, len(self._activity_groups), description=description)

    def _sport_to_activity(self):
        # sport_to_activity maps from the FIT sport field to the activity defined above.
        # more complex mapping is supported using kits (see acooke configuration),
        # but the top level must be a FIT field value for it to be recognized for monitor data
        # (which uses defaults only).
        return {SPORT_CYCLING: BIKE,
                SPORT_RUNNING: RUN,
                SPORT_SWIMMING: SWIM,
                SPORT_WALKING: WALK}

    def _all_groups_but_all(self):
        return [group for group in self._activity_groups.values() if group.name != ALL]

    def _record_to_db(self):
        # the mapping from FIT fields to database entries
        # you really don't want to alter this unless you know what you are doing...
        # todo - does this need to depend on activity group?
        return {'position_lat': (LATITUDE, DEG, StatisticJournalType.FLOAT),
                'position_long': (LONGITUDE, DEG, StatisticJournalType.FLOAT),
                'heart_rate': (HEART_RATE, BPM, StatisticJournalType.INTEGER),
                'enhanced_speed': (SPEED, MS, StatisticJournalType.FLOAT),
                'distance': (DISTANCE, KM, StatisticJournalType.FLOAT),
                'enhanced_altitude': (ALTITUDE, M, StatisticJournalType.FLOAT),
                'cadence': (CADENCE, RPM, StatisticJournalType.INTEGER)}

    def _load_activities_pipeline(self, s, c):
        sport_to_activity = self._sport_to_activity()
        record_to_db = self._record_to_db()
        add_activities(s, SegmentReader, c, owner_out=short_cls(SegmentReader),
                       sport_to_activity=sport_to_activity, record_to_db=record_to_db)

    def _ff_parameters(self):
        # each is a list of (days, start, scale) tuples.
        # for example, fitness with two different timescales:
        # fitness = ((42, 1, 1), (21, 1, 2))
        # https://andrewcooke.github.io/choochoo/ff-fitting
        fitness = ((42, 1, 1),)
        fatigue = ((7, 1, 5),)
        return fitness, fatigue

    def _impulse_groups(self):
        # activity groups that should have impulses calculated (ie that will contribute to FF statistics)
        return self._all_groups_but_all()

    def _load_power_statistics(self, s, c):
        # after elevation and before ff etc
        # defaults is none because configuration is complex
        pass

    def _load_ff_statistics(self, s, c, default_fthr=154):
        for group in self._impulse_groups():
            add_impulse(s, c, group)
            # we need a value here for various UI reasons.  might as well use my own value...
            add_activity_constant(s, group, FTHR, default_fthr,
                                  description=f'''
Heart rate (in bpm) at functional threshold for activities in the {group.name} group.

Your FTHR is the highest sustained heart rate you can maintain for long periods (an hour).
It is used to calculate how hard you are working (the Impulse) and, from that, 
your FF-model parameters (fitness and fatigue).
''',
                                  units=BPM, statistic_journal_type=StatisticJournalType.INTEGER)
        add_climb(s)  # default climb calculator
        fitness, fatigue = self._ff_parameters()
        add_responses(s, c, fitness=fitness, fatigue=fatigue)

    def _load_standard_statistics(self, s, c):
        add_statistics(s, ActivityCalculator, c, owner_in=short_cls(ResponseCalculator), climb=CLIMB_CNAME)
        add_statistics(s, SegmentCalculator, c, owner_in=short_cls(SegmentReader))
        add_statistics(s, MonitorCalculator, c, owner_in=short_cls(MonitorReader))
        add_statistics(s, KitCalculator, c, owner_in=short_cls(SegmentReader))

    def _load_summary_statistics(self, s, c):
        # need to call normalize here because schedule isn't a schedule type column,
        # but part of a kargs JSON blob.
        # also, add year first so that monthly doesn't get confused by extra stats range
        add_statistics(s, SummaryCalculator, c, schedule=Schedule.normalize('x'))
        add_statistics(s, SummaryCalculator, c, schedule=Schedule.normalize('y'))
        add_statistics(s, SummaryCalculator, c, schedule=Schedule.normalize('m'))

    def _load_statistics_pipeline(self, s, c):
        # order is important here because some pipelines expect values created by others
        # this converts RAW_ELEVATION to ELEVATION, if needed
        add_statistics(s, ElevationCalculator, c, owner_in='[unused - data via activity_statistics]')
        self._load_power_statistics(s, c)
        self._load_ff_statistics(s, c)
        self._load_standard_statistics(s, c)
        self._load_summary_statistics(s, c)
        add_statistics(s, AchievementCalculator, c, owner_in=short_cls(SegmentReader))

    def _load_diary_pipeline(self, s, c):
        add_displayer(s, DiaryDisplayer, c)
        add_displayer(s, MonitorDisplayer, c)
        # these tie-in to the constants used in add_impulse()
        fitness, fatigue = self._ff_parameters()
        all = self._activity_groups[ALL]
        add_displayer(s, ResponseDisplayer, c,
                      fitness=[name_constant(FITNESS_D % days, all) for (days, _, _) in fitness],
                      fatigue=[name_constant(FATIGUE_D % days, all) for (days, _, _) in fatigue])
        add_displayer(s, ActivityDisplayer, c)
        c2 = Counter()
        for delegate in self._activity_displayer_delegates():
            add_activity_displayer_delegate(s, delegate, c2)
        add_displayer(s, DatabaseDisplayer, c)

    def _activity_displayer_delegates(self):
        return [AchievementDelegate, ActivityDelegate, SegmentDelegate, NearbyDelegate, JupyterDelegate]

    def _load_monitor_pipeline(self, s, c):
        sport_to_activity = self._sport_to_activity()
        add_monitor(s, MonitorReader, c, sport_to_activity=sport_to_activity)

    def _load_constants(self, s):
        add_constant(s, SRTM1_DIR, base_system_path(self._base, version=PERMANENT, subdir='srtm1', create=False),
                     description='''
Directory containing STRM1 hgt files for elevations.

These data are used to give improved values when using GPS elevation.
You must create the directory and populate it with suitable files from http://dwtkns.com/srtm30m.
If the directory or files are missing the raw GPS elevation will be used.
This is noted as a warning in the logs (along with the name of the missing file).
''',
                     single=True, statistic_journal_type=StatisticJournalType.TEXT)
        add_constant(s, GARMIN_USER, None,
                     description='''
User for Garmin.
If set, monitor data (daily steps, heart rate) are downloaded from Garmin.
''',
                     single=True, statistic_journal_type=StatisticJournalType.TEXT)
        add_constant(s, GARMIN_PASSWORD, None,
                     description='''
Password for Garmin.
This is stored as plaintext on the server (and visible here)
so do not use an important password that applies to many accounts.
''',
                     single=True, statistic_journal_type=StatisticJournalType.TEXT)

    def _load_diary_topics(self, s, c):
        # the fields you see every day in the diary
        diary = add_diary_topic(s, 'Status', c)
        add_diary_topic_field(s, diary, 'Notes', c, StatisticJournalType.TEXT,
                              model={TYPE: EDIT}, description='Daily notes recorded by user in diary.')
        add_diary_topic_field(s, diary, 'Weight', c, StatisticJournalType.FLOAT,
                              units='kg', summary='[avg],[msr]', description='Weight recorded by user in diary.',
                              model={TYPE: FLOAT, LO: 50, HI: 100, DP: 1})
        add_diary_topic_field(s, diary, 'Sleep', c, StatisticJournalType.FLOAT,
                              units='h', summary='[avg]', description='Sleep time recorded by user in diary.',
                              model={TYPE: FLOAT, LO: 0, HI: 24, DP: 1})
        add_diary_topic_field(s, diary, 'Mood', c, StatisticJournalType.FLOAT,
                              summary='[avg]', description='Mood recorded by user in diary.',
                              model={TYPE: SCORE})
        add_diary_topic_field(s, diary, 'Medication', c, StatisticJournalType.TEXT,
                              summary='[cnt]', description='Medication recorded by user in diary.',
                              model={TYPE: EDIT})
        add_diary_topic_field(s, diary, 'Weather', c, StatisticJournalType.TEXT,
                              summary='[cnt]', description='Weather recorded by user in diary.',
                              model={TYPE: EDIT})

    def _load_activity_topics(self, s, c):
        # the fields in the diary that are displayed for each activity
        for activity_group in self._all_groups_but_all():
            c = Counter()
            add_activity_topic_field(s, None, ActivityTopicField.NAME, c, StatisticJournalType.TEXT,
                                     activity_group, model={TYPE: EDIT},
                                     description=ActivityTopicField.NAME_DESCRIPTION)
            # note that these have empty toic parents because they are children of the entry itself
            if activity_group.name != SWIM:
                add_activity_topic_field(s, None, 'Route', c, StatisticJournalType.TEXT,
                                         activity_group, model={TYPE: EDIT},
                                         description='Route recorded by user in diary.')
            add_activity_topic_field(s, None, NOTES, c, StatisticJournalType.TEXT,
                                     activity_group, model={TYPE: EDIT},
                                     description='Activity notes recorded by user in diary.')

    def _load_sys(self, sys, s):
        # finally, update the timezone
        DiaryTopicJournal.check_tz(sys, s)

