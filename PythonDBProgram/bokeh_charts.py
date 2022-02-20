from turtle import width
from bokeh.io import output_file, show
from bokeh.plotting import figure
from numpy import append
from release import sql_get_release_counts

output_file("./PythonDBProgram/bokeh.html")

def bk_band_releases():
    query = sql_get_release_counts()

    bands = []
    counts = []
    for item in query:
        bands.append(item[1] + " (ID %s)"%item[0])
        counts.append(item[2])

    p = figure(x_range=bands, height=500, width=1500, title="Releases",
            toolbar_location=None, tools="")

    p.vbar(x=bands, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)