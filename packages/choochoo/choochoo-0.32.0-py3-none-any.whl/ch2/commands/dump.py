
from logging import getLogger

import pandas as pd

from .args import SUB_COMMAND, START, FINISH, NAMES, \
    OWNER, CONSTRAINT, SCHEDULE, SOURCE_ID, STATISTIC_QUARTILES, PRINT, FORMAT, \
    CSV, DESCRIBE, MAX_COLUMNS, MAX_ROWS, WIDTH, MAX_COLWIDTH, TABLE, NAME, STATISTICS, GROUP
from ..data import df, statistics, statistic_quartiles
from ..sql import *
from ..sql.support import Base

# to stop the import * from being deleted
StatisticName

log = getLogger(__name__)


def dump(args, system, db):
    '''
## dump

    > ch2 dump COMMAND

Simple access to the database - similar to the interface provided in Jupyter notebooks,
but accessed from the command line.

The format can be selected with `--print` (the default), `--csv` and `--describe`.

For full options see `ch2 data -h` and `ch2 data COMMAND -h`

### Examples

    > ch2 dump --csv table StatisticName

Will print the contents of the StatisticName table in CSV format.

    > ch2 dump statistics '%HR%' --group Bike --start 2018-01-01

Will print HR-related statistics from the start of 2018 for the given activity group.
    '''

    with db.session_context() as s:

        if args[SUB_COMMAND] == TABLE:
            name = args[NAME]
            if name in globals():
                table = globals()[name]
                log.debug(f'Found {table}/{type(table)}')
                if issubclass(table.__class__, Base.__class__):
                    frame = df(s.query(table))
                else:
                    raise Exception('%s is not a mapped table' % name)
            else:
                raise Exception('%s does not exist' % name)
        elif args[SUB_COMMAND] == STATISTICS:
            frame = statistics(s, *args[NAMES], start=args[START], finish=args[FINISH],
                               owner=args[OWNER], activity_group=args[GROUP],
                               sources=[Source.from_id(s, int(id)) for id in args[SOURCE_ID]])
        elif args[SUB_COMMAND] == STATISTIC_QUARTILES:
            frame = statistic_quartiles(s, *args[NAMES], start=args[START], finish=args[FINISH],
                                        owner=args[OWNER], activity_group=args[GROUP], schedule=args[SCHEDULE],
                                        sources=[Source.from_id(s, int(id)) for id in args[SOURCE_ID]])
        else:
            raise Exception('Unexpected %s: %s' % (SUB_COMMAND, args[SUB_COMMAND]))

        pd.options.display.max_columns = args[MAX_COLUMNS]
        if args[MAX_COLWIDTH] is not None: pd.options.display.max_colwidth = args[MAX_COLWIDTH]
        pd.options.display.max_rows = args[MAX_ROWS]
        pd.options.display.width = args[WIDTH]

        if args[FORMAT] == PRINT:
            print(frame)
        elif args[FORMAT] == CSV:
            print(frame.to_csv())
        elif args[FORMAT] == DESCRIBE:
            print(frame.describe(include='all'))
