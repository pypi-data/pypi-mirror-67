import re

POW_M1 = '\u207b\u00b9'
POW_2 = '\u00b2'

AGE = 'Age'
ACTIVE_DISTANCE = 'Active Distance'
ACTIVE_SPEED = 'Active Speed'
ACTIVE_TIME = 'Active Time'
ACTIVITY = 'Activity'
ACTIVITY_GROUP = 'Activity Group'
AIR_SPEED = 'Air Speed'
ALL = 'All'
ANY_ALL = '% All'
ALTITUDE = 'Altitude'
ASPECT_RATIO = 'Aspect Ratio'
BOOKMARK = 'Bookmark'
CADENCE = 'Cadence'
CALORIE_ESTIMATE = 'Calorie Estimate'
CDA = 'CdA'
CLIMB = 'Climb'
CLIMB_CATEGORY = 'Climb Category'
CLIMB_DISTANCE = 'Climb Distance'
CLIMB_ELEVATION = 'Climb Elevation'
CLIMB_GRADIENT = 'Climb Gradient'
CLIMB_TIME = 'Climb Time'
CLIMB_POWER = 'Climb Power'
COLOR = 'Color'
COVERAGE = 'Coverage'
CRR = 'Crr'
CUMULATIVE_STEPS = 'Cumulative Steps'
CUMULATIVE_STEPS_START = 'Cumulative Steps Start'
CUMULATIVE_STEPS_FINISH = 'Cumulative Steps Finish'
DAILY_STEPS = 'Daily Steps'
DELAYED_POWER = 'Delayed Power'
DETRENDED_HEART_RATE = 'Detrended Heart Rate'
DIRECTION = 'Direction'
DISTANCE = 'Distance'
DUMMY = 'Dummy'
EARNED_D = 'Earned %d'
EARNED_D_ANY= 'Earned %'
ELEVATION = 'Elevation'
ENERGY = 'Energy'
ENERGY_ESTIMATE = 'Energy Estimate'
FATIGUE = 'Fatigue'
FINISH = 'Finish'
FITNESS = 'Fitness'
FATIGUE_D = 'Fatigue %dd'
FATIGUE_D_ANY = 'Fatigue %'
FITNESS_D = 'Fitness %dd'
FITNESS_D_ANY = 'Fitness %'
FTHR = 'FTHR'
GRADE = 'Grade'
GROUP = 'Group'
HEADING = 'Heading'
HEART_RATE = 'Heart Rate'
HR_IMPULSE_10 = 'HR Impulse / 10s'
HR_ZONE = 'HR Zone'
INDEX = 'Index'
KIT_ADDED = 'Kit Added'
KIT_RETIRED = 'Kit Retired'
KIT_USED = 'Kit Used'
LATITUDE = 'Latitude'
LIFETIME = 'Lifetime'
LOCAL_TIME = 'Date'
LONGITUDE = 'Longitude'
LOSS = 'Loss'
MAX_MEAN_PE_M = 'Max Mean PE %dm'
MAX_MEAN_PE_M_ANY = 'Max Mean PE %'
MAX_MED_HR_M = 'Max Med HR %dm'
MAX_MED_HR_M_ANY = 'Max Med HR %'
MEAN_POWER_ESTIMATE = 'Mean Power Estimate'
MED_KM_TIME = 'Med %dkm Time'
MED_KM_TIME_ANY = 'Med % Time'
MIN_KM_TIME = 'Min %dkm Time'
MIN_KM_TIME_ANY = 'Min % Time'
MIXED = 'Mixed'
PERCENT_IN_Z = 'Percent in Z%d'
PERCENT_IN_Z_ANY = 'Percent in Z%'
PLATEAU_D = 'Plateau %d'
PLATEAU_D_ANY = 'Plateau %'
POWER_ESTIMATE = 'Power Estimate'
PREDICTED_HEART_RATE = 'Predicted Heart Rate'
RECOVERY_D = 'Recovery %d'
RECOVERY_D_ANY = 'Recovery %'
SEGMENT_TIME = 'Segment Time'
SEGMENT_DISTANCE = 'Segment Distance'
SEGMENT_HEART_RATE = 'Segment Heart Rate'
SOURCE = 'Source'
SPEED = 'Speed'
SPHERICAL_MERCATOR_X = 'Spherical Mercator X'
SPHERICAL_MERCATOR_Y = 'Spherical Mercator Y'
START = 'Start'
STEPS = 'Steps'
RAW_ELEVATION = 'Raw Elevation'
REST_HR = 'Rest HR'
TIME = 'Time'
TIME_IN_Z = 'Time in Z%d'
TIME_IN_Z_ANY = 'Time in Z%'
TIMESPAN_ID = 'Timespan ID'
TOTAL_CLIMB = 'Total Climb'

SPORT_CYCLING = 'cycling'
SPORT_RUNNING = 'running'
SPORT_SWIMMING = 'swimming'
SPORT_WALKING = 'walking'
SPORT_GENERIC = 'generic'

# todo - there is no need for these silly square brackets - remove?
# ahhh. something about allowing parsing with splitting on commas?
MAX = '[max]'
MIN = '[min]'
CNT = '[cnt]'
AVG = '[avg]'
SUM = '[sum]'
MSR = '[msr]'   # measure (separate table, less efficient)
def summaries(*args): return ','.join(args)


BPM = 'bpm'
D = 'd'
DEG = 'deg'
FF = 'FF'
H = 'h'
J = 'J'
KJ = 'kJ'
KCAL = 'kCal'
KG = 'kg'
KM = 'km'
KMH = f'kmh{POW_M1}'
M = 'm'
MS = f'ms{POW_M1}'
PC = '%'
RPM = 'rpm'
S = 's'
STEPS_UNITS = 'stp'
W = 'W'


def _cov(name): return f'Cov {name}'  # coverage
def _delta(name): return f'Δ {name}'
def _avg(name): return f'Avg {name}'
def _slash(name, units): return f'{name} / {units}'
def _log(name): return f'Log {name}'
def _sqr(name): return f'{name}{POW_2}'
def _new(name): return f'New {name}'
def _src(name): return f'Src {name}'
def _lo(name): return f'Lo {name}'
def _hi(name): return f'Hi {name}'
def _s(name): return f'{name}s'

MED_WINDOW = '60s'
def _med(name): return f'Med{MED_WINDOW} {name}'

def like(pattern, names):
    return list(_like(pattern, names))

def _like(pattern, names, test=True):
    matcher = re.compile(re.sub('%', '.+', pattern))
    for name in names:
        if bool(matcher.match(name)) == test:
            yield name

def unlike(pattern, names):
    return list(_like(pattern, names, test=False))


LO_REST_HR = _lo(REST_HR)
HI_REST_HR = _hi(REST_HR)

AIR_SPEED_2 = _sqr(AIR_SPEED)
AVG_AIR_SPEED_2 = _avg(AIR_SPEED_2)
DELTA_AIR_SPEED_2 = _delta(AIR_SPEED_2)

SPEED_2 = _sqr(SPEED)
AVG_SPEED_2 = _avg(SPEED_2)
DELTA_SPEED_2 = _delta(SPEED_2)

DELTA_TIME = _delta(TIME)
DELTA_DISTANCE = _delta(DISTANCE)
DELTA_ELEVATION = _delta(ELEVATION)
DELTA_SPEED = _delta(SPEED)
DELTA_ENERGY = _delta(ENERGY)

ACTIVE_DISTANCE_KM = _slash(ACTIVE_DISTANCE, KM)
ACTIVE_TIME_H = _slash(ACTIVE_TIME, H)
CLIMB_MS = _slash(CLIMB, MS)
DISTANCE_KM = _slash(DISTANCE, KM)
ELEVATION_M = _slash(ELEVATION, M)
GRADE_PC = _slash(GRADE, PC)
HEART_RATE_BPM = _slash(HEART_RATE, BPM)
SPEED_KMH = _slash(SPEED, KMH)
POWER_ESTIMATE_W = _slash(POWER_ESTIMATE, W)

MED_SPEED_KMH = _med(SPEED_KMH)
MED_HEART_RATE_BPM = _med(HEART_RATE_BPM)
MED_HR_IMPULSE_10 = _med(HR_IMPULSE_10)
MED_CADENCE = _med(CADENCE)
MED_POWER_ESTIMATE_W = _med(POWER_ESTIMATE_W)

POWER_HR = 'Power / HR'
POWER_HR_LAG = 'Power / HR Lag'
HR_DRIFT = 'HR Drift'
LOG_HR_DRIFT = _log('HR Drift')
IDLE_HR = 'Idle HR'
WIND_SPEED = 'Wind Speed'
WIND_HEADING = 'Wind Heading'

