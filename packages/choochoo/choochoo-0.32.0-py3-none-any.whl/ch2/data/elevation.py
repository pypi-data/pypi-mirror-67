
from logging import getLogger

from scipy.interpolate import UnivariateSpline

from .frame import present
from ..names import ELEVATION, DISTANCE, RAW_ELEVATION, GRADE


log = getLogger(__name__)


def smooth_elevation(df, smooth=4):
    if not present(df, ELEVATION):
        log.debug(f'Smoothing {RAW_ELEVATION} to get {ELEVATION}')
        unique = df.loc[~df[DISTANCE].isna() & ~df[RAW_ELEVATION].isna(),
                        [DISTANCE, RAW_ELEVATION]].drop_duplicates(DISTANCE)
        # the smoothing factor is from eyeballing results only.  maybe it should be a parameter.
        # it seems better to smooth along the route rather that smooth the terrain model since
        # 1 - we expect the route to be smoother than the terrain in general (roads / tracks)
        # 2 - smoothing the 2d terrain is difficult to control and can give spikes
        # 3 - we better handle errors from mismatches between terrain model and position
        #     (think hairpin bends going up a mountainside)
        # the main drawbacks are
        # 1 - speed on loading
        # 2 - no guarantee of consistency between routes (or even on the same routine retracing a path)
        spline = UnivariateSpline(unique[DISTANCE], unique[RAW_ELEVATION], s=len(unique) * smooth)
        df[ELEVATION] = spline(df[DISTANCE])
        df[GRADE] = (spline.derivative()(df[DISTANCE]) * 100)  # two step to use rolling from pandas
        df[GRADE] = df[GRADE].rolling(5, center=True).median().ffill().bfill()
        # avoid extrapolation / interpolation
        df.loc[df[RAW_ELEVATION].isna(), [ELEVATION]] = None
    return df
