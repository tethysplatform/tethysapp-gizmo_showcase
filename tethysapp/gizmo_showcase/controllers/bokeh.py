from math import pi
import numpy as np
import pandas as pd
from django.shortcuts import render
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, RangeTool, HoverTool
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum, dodge
from bokeh.sampledata.penguins import data as penguin_data
from bokeh.sampledata.stocks import AAPL
from bokeh.transform import factor_cmap, factor_mark
from tethys_sdk.gizmos import BokehView
from tethys_sdk.base import controller
from .common import docs_endpoint


@controller
def bokeh_view(request):
    """
    Controller for the Bokeh View page.
    """
    # Scatter plot
    SPECIES = sorted(penguin_data.species.unique())
    MARKERS = ['hex', 'circle_x', 'triangle']

    scatter_fig = figure(title = "Penguin size", background_fill_color="#fafafa")
    scatter_fig.xaxis.axis_label = 'Flipper Length (mm)'
    scatter_fig.yaxis.axis_label = 'Body Mass (g)'

    scatter_fig.scatter("flipper_length_mm", "body_mass_g", source=penguin_data,
            legend_group="species", fill_alpha=0.4, size=12,
            marker=factor_mark('species', MARKERS, SPECIES),
            color=factor_cmap('species', 'Category10_3', SPECIES))

    scatter_fig.legend.location = "top_left"
    scatter_fig.legend.title = "Species"
    scatter_plot = BokehView(scatter_fig)
    
    # Line plot
    line_x = np.linspace(0, 4*np.pi, 100)
    line_y = np.sin(line_x)

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save,box_select"

    line_fig = figure(title="Legend Example", tools=TOOLS)

    line_fig.line(line_x,   line_y, legend_label="sin(x)")
    line_fig.line(line_x, 2*line_y, legend_label="2*sin(x)", color="orange")
    line_fig.line(line_x, 3*line_y, legend_label="3*sin(x)", color="green")

    line_fig.legend.title = 'Example Title'
    line_plot = BokehView(line_fig)
    
    # Pie plot
    pie_x = {
        'United States': 157,
        'United Kingdom': 93,
        'Japan': 89,
        'China': 63,
        'Germany': 44,
        'India': 42,
        'Italy': 40,
        'Australia': 35,
        'Brazil': 32,
        'France': 31,
        'Taiwan': 31,
        'Spain': 29
    }

    pie_data = pd.Series(pie_x).reset_index(name='value').rename(columns={'index': 'country'})
    pie_data['angle'] = pie_data['value']/pie_data['value'].sum() * 2*pi
    pie_data['color'] = Category20c[len(pie_x)]

    pie_fig = figure(height=350, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

    pie_fig.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='country', source=pie_data)

    pie_fig.axis.axis_label = None
    pie_fig.axis.visible = False
    pie_fig.grid.grid_line_color = None
    
    pie_plot = BokehView(pie_fig)
    
    # Bar chart
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ['2015', '2016', '2017']

    bar_data = {'fruits' : fruits,
            '2015'   : [2, 1, 4, 3, 2, 4],
            '2016'   : [5, 3, 3, 2, 4, 6],
            '2017'   : [3, 2, 4, 4, 5, 3]}

    source = ColumnDataSource(data=bar_data)

    bar_fig = figure(x_range=fruits, y_range=(0, 10), title="Fruit Counts by Year",
            height=350, toolbar_location=None, tools="")

    bar_fig.vbar(x=dodge('fruits', -0.25, range=bar_fig.x_range), top='2015', source=source,
        width=0.2, color="#c9d9d3", legend_label="2015")

    bar_fig.vbar(x=dodge('fruits',  0.0,  range=bar_fig.x_range), top='2016', source=source,
        width=0.2, color="#718dbf", legend_label="2016")

    bar_fig.vbar(x=dodge('fruits',  0.25, range=bar_fig.x_range), top='2017', source=source,
        width=0.2, color="#e84d60", legend_label="2017")

    bar_fig.x_range.range_padding = 0.1
    bar_fig.xgrid.grid_line_color = None
    bar_fig.legend.location = "top_left"
    bar_fig.legend.orientation = "horizontal"
    
    bar_chart = BokehView(bar_fig)
    
    # Time series
    dates = np.array(AAPL['date'], dtype=np.datetime64)
    source = ColumnDataSource(data=dict(date=dates, close=AAPL['adj_close']))

    time_series_fig = figure(height=300, width=800, tools="xpan", toolbar_location=None,
                             x_axis_type="datetime", x_axis_location="above",
                             background_fill_color="#efefef", x_range=(dates[1500], dates[2500]))

    time_series_fig.line('date', 'close', source=source)
    time_series_fig.yaxis.axis_label = 'Price'

    select = figure(title="Drag the middle and edges of the selection box to change the range above",
                    height=130, width=800, y_range=time_series_fig.y_range,
                    x_axis_type="datetime", y_axis_type=None,
                    tools="", toolbar_location=None, background_fill_color="#efefef")

    range_tool = RangeTool(x_range=time_series_fig.x_range)
    range_tool.overlay.fill_color = "navy"
    range_tool.overlay.fill_alpha = 0.2

    select.line('date', 'close', source=source)
    select.ygrid.grid_line_color = None
    select.add_tools(range_tool)
    select.toolbar.active_multi = range_tool
    
    time_series_plot = BokehView(column(time_series_fig, select))
    
    # Hexbin plot
    n = 500
    hex_x = 2 + 2*np.random.standard_normal(n)
    hex_y = 2 + 2*np.random.standard_normal(n)

    hex_fig = figure(title="Hexbin for 500 points", match_aspect=True,
            tools="wheel_zoom,reset", background_fill_color='#440154')
    hex_fig.grid.visible = False

    hex_r, _ = hex_fig.hexbin(hex_x, hex_y, size=0.5, hover_color="pink", hover_alpha=0.8)

    hex_fig.circle(hex_x, hex_y, color="white", size=1)

    hex_fig.add_tools(HoverTool(
        tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
        mode="mouse", point_policy="follow_mouse", renderers=[hex_r]
    ))
    
    hexbin_plot = BokehView(hex_fig)

    context = {
        'docs_endpoint': docs_endpoint,
        'scatter_plot': scatter_plot,
        'line_plot': line_plot,
        'pie_plot': pie_plot,
        'bar_chart': bar_chart,
        'time_series_plot': time_series_plot,
        'hexbin_plot': hexbin_plot,
    }
    return render(request, 'gizmo_showcase/bokeh_view.html', context)
