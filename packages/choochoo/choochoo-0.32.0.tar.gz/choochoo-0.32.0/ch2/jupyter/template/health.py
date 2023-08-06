
import datetime as dt

from bokeh.io import output_file
from bokeh.layouts import column
from bokeh.plotting import show

from ch2.data import *
from ch2.jupyter.decorator import template


@template
def health():

    '''
    # Health
    '''

    '''
    $contents
    '''

    '''
    ## Load Data
    
    Open a connection to the database and load the data we require.
    '''

    s = session('-v2')
    health = std_health_statistics(s)

    '''
    ## Health and Fitness
    '''

    output_file(filename='/dev/null')

    fitness, fatigue = like(FITNESS_D_ANY, health.columns), like(FATIGUE_D_ANY, health.columns)
    colours = ['black'] * len(fitness) + ['red'] * len(fatigue)
    alphas = [1.0] * len(fitness) + [0.5] * len(fatigue)
    ff = multi_line_plot(900, 300, TIME, fitness + fatigue, health, colours, alphas=alphas)
    add_multi_line_at_index(ff, TIME, fitness + fatigue, health, colours, alphas=alphas, index=-1)
    atd = std_distance_time_plot(900, 200, health, x_range=ff.x_range)
    shr = multi_plot(900, 200, TIME, [DAILY_STEPS, REST_HR], health, ['grey', 'red'], alphas=[1, 0.5],
                     x_range=ff.x_range, rescale=True, plotters=[bar_plotter(dt.timedelta(hours=20)), dot_plotter()])
    add_band(shr, TIME, LO_REST_HR, HI_REST_HR, health, 'red', alpha=0.1, y_range_name=REST_HR)
    add_curve(shr, TIME, REST_HR, health, color='red', y_range_name=REST_HR)
    show(column(ff, atd, shr))
