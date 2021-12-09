import datetime as dt
from django.shortcuts import render
from plotly import graph_objs as go
from bokeh.plotting import figure as bokeh_figure
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import LinePlot, BarPlot, ScatterPlot, \
    PiePlot, TimeSeries, PolarPlot, AreaRange, PlotlyView, BokehView
from .common import docs_endpoint


@login_required()
def plot_view(request):
    """
    Controller for the Plot View page.
    """
    line_plot_view = LinePlot(height='500px',
                              width='500px',
                              engine='highcharts',
                              title='Plot Title',
                              subtitle='Plot Subtitle',
                              spline=True,
                              x_axis_title='Altitude',
                              x_axis_units='km',
                              y_axis_title='Temperature',
                              y_axis_units='°C',
                              series=[
                                  {
                                      'name': 'Air Temp',
                                      'color': '#0066ff',
                                      'marker': {'enabled': False},
                                      'data': [
                                          [0, 5], [10, -70],
                                          [20, -86.5], [30, -66.5],
                                          [40, -32.1],
                                          [50, -12.5], [60, -47.7],
                                          [70, -85.7], [80, -106.5]
                                      ]
                                  },
                                  {
                                      'name': 'Water Temp',
                                      'color': '#ff6600',
                                      'data': [
                                          [0, 15], [10, -50],
                                          [20, -56.5], [30, -46.5],
                                          [40, -22.1],
                                          [50, -2.5], [60, -27.7],
                                          [70, -55.7], [80, -76.5]
                                      ]
                                  }
                              ]
                              )
    
    # D3 Line Plot View
    d3_line_plot_view = LinePlot(height='500px',
                                 width='100%',
                                 engine='d3',
                                 title='Plot Title',
                                 subtitle='Plot Subtitle',
                                 spline=True,
                                 x_axis_title='Altitude',
                                 x_axis_units='km',
                                 y_axis_title='Temperature',
                                 y_axis_units='°C',
                                 series=[
                                     {
                                         'name': 'Air Temp',
                                         'data': [
                                             [0, 5], [10, -70],
                                             [20, -86.5], [30, -66.5],
                                             [40, -32.1],
                                             [50, -12.5], [60, -47.7],
                                             [70, -85.7], [80, -106.5]
                                         ]
                                     },
                                     {
                                         'name': 'Water Temp',
                                         'data': [
                                             [0, 15], [10, -50],
                                             [20, -56.5], [30, -46.5],
                                             [40, -22.1],
                                             [50, -2.5], [60, -27.7],
                                             [70, -55.7], [80, -76.5]
                                         ]
                                     }
                                 ]
                                 )

    # Plot Views
    male_dataset = {
        'name': 'Male',
        'color': '#0066ff',
        'data': [
            [174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6],
            [187.2, 78.8], [181.5, 74.8], [184.0, 86.4], [184.5, 78.4],
            [175.0, 62.0], [184.0, 81.6], [180.0, 76.6], [177.8, 83.6],
            [192.0, 90.0], [176.0, 74.6], [174.0, 71.0], [184.0, 79.6],
            [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9],
            [176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4],
            [173.5, 81.8], [178.0, 89.6], [180.3, 82.8], [180.3, 76.4],
            [164.5, 63.2], [173.0, 60.9], [183.5, 74.8], [175.5, 70.0],
            [188.0, 72.4], [189.2, 84.1], [172.8, 69.1], [170.0, 59.5],
            [182.0, 67.2], [170.0, 61.3], [177.8, 68.6], [184.2, 80.1],
            [186.7, 87.8], [171.4, 84.7], [172.7, 73.4], [175.3, 72.1],
            [180.3, 82.6], [182.9, 88.7], [188.0, 84.1], [177.2, 94.1],
            [172.1, 74.9], [167.0, 59.1], [169.5, 75.6], [174.0, 86.2],
            [172.7, 75.3], [182.2, 87.1], [164.1, 55.2], [163.0, 57.0],
            [171.5, 61.4], [184.2, 76.8], [174.0, 86.8], [174.0, 72.2],
            [177.0, 71.6], [186.0, 84.8], [167.0, 68.2], [171.8, 66.1]
        ]
    }

    female_dataset = {
        'name': 'Female',
        'color': '#ff6600',
        'data': [
            [161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0],
            [155.8, 53.6], [170.0, 59.0], [159.1, 47.6], [166.0, 69.8],
            [176.2, 66.8], [160.2, 75.2], [172.5, 55.2], [170.9, 54.2],
            [172.9, 62.5], [153.4, 42.0], [160.0, 50.0], [147.2, 49.8],
            [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8],
            [159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8],
            [170.2, 72.8], [174.0, 54.5], [173.0, 59.8], [179.9, 67.3],
            [170.5, 67.8], [160.0, 47.0], [154.4, 46.2], [162.0, 55.0],
            [176.5, 83.0], [160.0, 54.4], [152.0, 45.8], [162.1, 53.6],
            [170.0, 73.2], [160.2, 52.1], [161.3, 67.9], [166.4, 56.6],
            [168.9, 62.3], [163.8, 58.5], [167.6, 54.5], [160.0, 50.2],
            [161.3, 60.3], [167.6, 58.3], [165.1, 56.2], [160.0, 50.2],
            [170.0, 72.9], [157.5, 59.8], [167.6, 61.0], [160.7, 69.1],
            [163.2, 55.9], [152.4, 46.5], [157.5, 54.3], [168.3, 54.8],
            [180.3, 60.7], [165.5, 60.0], [165.0, 62.0], [164.5, 60.3]
        ]
    }

    scatter_plot_view = ScatterPlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Scatter Plot',
        subtitle='Scatter Plot',
        x_axis_title='Height',
        x_axis_units='cm',
        y_axis_title='Weight',
        y_axis_units='kg',
        series=[male_dataset, female_dataset]
    )

    # D3 Scatter Plot
    d3_scatter_plot_view = ScatterPlot(
        width='100%',
        height='500px',
        engine='d3',
        title='D3 Scatter Plot',
        subtitle='D3 Scatter Plot',
        x_axis_title='Height',
        x_axis_units='cm',
        y_axis_title='Weight',
        y_axis_units='kg',
        series=[male_dataset, female_dataset]
    )

    # Web Plot
    web_plot = PolarPlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Polar Chart',
        subtitle='Polar Chart',
        pane={
            'size': '80%'
        },
        categories=['Infiltration', 'Soil Moisture', 'Precipitation',
                    'Evaporation', 'Roughness', 'Runoff', 'Permeability',
                    'Vegetation'],
        series=[
            {
                'name': 'Park City',
                'data': [0.2, 0.5, 0.1, 0.8, 0.2, 0.6, 0.8, 0.3],
                'pointPlacement': 'on'
            },
            {
                'name': 'Little Dell',
                'data': [0.8, 0.3, 0.2, 0.5, 0.1, 0.8, 0.2, 0.6],
                'pointPlacement': 'on'
            }
        ]
    )

    # Pie Plot
    pie_plot_view = PiePlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Pie Chart',
        subtitle='Pie Chart',
        series=[{
            'type': 'pie',
            'name': 'Browser share',
            'data': [
                ['Firefox', 45.0],
                ['IE', 26.8],
                {
                    'name': 'Chrome',
                    'y': 12.8,
                    'sliced': True,
                    'selected': True
                },
                ['Safari', 8.5],
                ['Opera', 6.2],
                ['Others', 0.7]
            ]
        }]
    )

    # D3 Pie Plot
    d3_pie_plot_view = PiePlot(width='100%',
                               height='500px',
                               engine='d3',
                               title='Pie Chart',
                               subtitle='Pie Chart',
                               series=[
                                   {'name': 'Firefox', 'value': 45.0},
                                   {'name': 'IE', 'value': 26.8},
                                   {'name': 'Chrome', 'value': 12.8},
                                   {'name': 'Safari', 'value': 8.5},
                                   {'name': 'Opera', 'value': 8.5},
                                   {'name': 'Others', 'value': 0.7}
                               ])

    # Bar Plot
    bar_plot_view = BarPlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Bar Chart',
        subtitle='Bar Chart',
        vertical=False,
        categories=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ],
        axis_units='millions',
        axis_title='Population',
        series=[{
            'name': 'Year 1800',
            'data': [107, 31, 635, 203, 2]
        }, {
            'name': 'Year 1900',
            'data': [133, 156, 947, 408, 6]
        }, {
            'name': 'Year 2008',
            'data': [973, 914, 4054, 732, 34]}
        ]
    )

    # D3 Bar Plot
    d3_bar_plot_view = BarPlot(
        width='100%',
        title='Bar Chart',
        subtitle='Bar Chart',
        vertical=True,
        categories=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ],
        axis_units='millions',
        axis_title='Population',
        series=[{
            'name': "Year 1800",
            'data': [100, 31, 635, 203, 275, 487, 872, 671, 736, 568, 487, 432]
        }, {
            'name': "Year 1900",
            'data': [133, 200, 947, 408, 682, 328, 917, 171, 482, 140, 176, 237]
        }, {
            'name': "Year 2000",
            'data': [764, 628, 300, 134, 678, 200, 781, 571, 773, 192, 836, 172]
        }, {
            'name': "Year 2008",
            'data': [973, 914, 500, 400, 349, 108, 372, 726, 638, 927, 621, 364]
        }
        ]
    )

    # Time series plot
    timeseries_plot = TimeSeries(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Irregular Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008',
            'data': [
                [dt.datetime(2008, 12, 2), 0.8],
                [dt.datetime(2008, 12, 9), 0.6],
                [dt.datetime(2008, 12, 16), 0.6],
                [dt.datetime(2008, 12, 28), 0.67],
                [dt.datetime(2009, 1, 1), 0.81],
                [dt.datetime(2009, 1, 8), 0.78],
                [dt.datetime(2009, 1, 12), 0.98],
                [dt.datetime(2009, 1, 27), 1.84],
                [dt.datetime(2009, 2, 10), 1.80],
                [dt.datetime(2009, 2, 18), 1.80],
                [dt.datetime(2009, 2, 24), 1.92],
                [dt.datetime(2009, 3, 4), 2.49],
                [dt.datetime(2009, 3, 11), 2.79],
                [dt.datetime(2009, 3, 15), 2.73],
                [dt.datetime(2009, 3, 25), 2.61],
                [dt.datetime(2009, 4, 2), 2.76],
                [dt.datetime(2009, 4, 6), 2.82],
                [dt.datetime(2009, 4, 13), 2.8],
                [dt.datetime(2009, 5, 3), 2.1],
                [dt.datetime(2009, 5, 26), 1.1],
                [dt.datetime(2009, 6, 9), 0.25],
                [dt.datetime(2009, 6, 12), 0]
            ]
        }, {
            'name': 'Winter test',
            'data': [
                [dt.datetime(2008, 12, 2), 1.8],
                [dt.datetime(2008, 12, 9), 1.6],
                [dt.datetime(2008, 12, 16), 1.6],
                [dt.datetime(2008, 12, 28), 1.67],
                [dt.datetime(2009, 1, 1), 1.81],
                [dt.datetime(2009, 1, 8), 1.78],
                [dt.datetime(2009, 1, 12), 1.98],
                [dt.datetime(2009, 1, 27), 2.84],
                [dt.datetime(2009, 2, 10), 2.80],
                [dt.datetime(2009, 2, 18), 2.80],
                [dt.datetime(2009, 2, 24), 2.92],
                [dt.datetime(2009, 3, 4), 3.49],
                [dt.datetime(2009, 3, 11), 3.79],
                [dt.datetime(2009, 3, 15), 3.73],
                [dt.datetime(2009, 3, 25), 3.61],
                [dt.datetime(2009, 4, 2), 3.76],
                [dt.datetime(2009, 4, 6), 3.82],
                [dt.datetime(2009, 4, 13), 3.8],
                [dt.datetime(2009, 5, 3), 3.1],
                [dt.datetime(2009, 5, 26), 2.1],
                [dt.datetime(2009, 6, 9), 1.25],
                [dt.datetime(2009, 6, 12), 0]
            ]
        }]
    )

    # D3 Time series plot
    d3_timeseries_plot_view = TimeSeries(
        width='100%',
        title='Irregular Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008',
            'data': [
                [dt.datetime(2008, 12, 2), 0.8],
                [dt.datetime(2008, 12, 9), 0.6],
                [dt.datetime(2008, 12, 16), 0.6],
                [dt.datetime(2008, 12, 28), 0.67],
                [dt.datetime(2009, 1, 1), 0.81],
                [dt.datetime(2009, 1, 8), 0.78],
                [dt.datetime(2009, 1, 12), 0.98],
                [dt.datetime(2009, 1, 27), 1.84],
                [dt.datetime(2009, 2, 10), 1.80],
                [dt.datetime(2009, 2, 18), 1.80],
                [dt.datetime(2009, 2, 24), 1.92],
                [dt.datetime(2009, 3, 4), 2.49],
                [dt.datetime(2009, 3, 11), 2.79],
                [dt.datetime(2009, 3, 15), 2.73],
                [dt.datetime(2009, 3, 25), 2.61],
                [dt.datetime(2009, 4, 2), 2.76],
                [dt.datetime(2009, 4, 6), 2.82],
                [dt.datetime(2009, 4, 13), 2.8],
                [dt.datetime(2009, 5, 3), 2.1],
                [dt.datetime(2009, 5, 26), 1.1],
                [dt.datetime(2009, 6, 9), 0.25],
                [dt.datetime(2009, 6, 12), 0]
            ]
        }, {
            'name': 'Winter test',
            'data': [
                [dt.datetime(2008, 12, 2), 1.8],
                [dt.datetime(2008, 12, 9), 1.6],
                [dt.datetime(2008, 12, 16), 1.6],
                [dt.datetime(2008, 12, 28), 1.67],
                [dt.datetime(2009, 1, 1), 1.81],
                [dt.datetime(2009, 1, 8), 1.78],
                [dt.datetime(2009, 1, 12), 1.98],
                [dt.datetime(2009, 1, 27), 2.84],
                [dt.datetime(2009, 2, 10), 2.80],
                [dt.datetime(2009, 2, 18), 2.80],
                [dt.datetime(2009, 2, 24), 2.92],
                [dt.datetime(2009, 3, 4), 3.49],
                [dt.datetime(2009, 3, 11), 3.79],
                [dt.datetime(2009, 3, 15), 3.73],
                [dt.datetime(2009, 3, 25), 3.61],
                [dt.datetime(2009, 4, 2), 3.76],
                [dt.datetime(2009, 4, 6), 3.82],
                [dt.datetime(2009, 4, 13), 3.8],
                [dt.datetime(2009, 5, 3), 3.1],
                [dt.datetime(2009, 5, 26), 2.1],
                [dt.datetime(2009, 6, 9), 1.25],
                [dt.datetime(2009, 6, 12), 0]
            ]
        }]
    )

    averages = [
        [dt.datetime(2009, 7, 1), 21.5], [dt.datetime(2009, 7, 2), 22.1], [dt.datetime(2009, 7, 3), 23],
        [dt.datetime(2009, 7, 4), 23.8], [dt.datetime(2009, 7, 5), 21.4], [dt.datetime(2009, 7, 6), 21.3],
        [dt.datetime(2009, 7, 7), 18.3], [dt.datetime(2009, 7, 8), 15.4], [dt.datetime(2009, 7, 9), 16.4],
        [dt.datetime(2009, 7, 10), 17.7], [dt.datetime(2009, 7, 11), 17.5], [dt.datetime(2009, 7, 12), 17.6],
        [dt.datetime(2009, 7, 13), 17.7], [dt.datetime(2009, 7, 14), 16.8], [dt.datetime(2009, 7, 15), 17.7],
        [dt.datetime(2009, 7, 16), 16.3], [dt.datetime(2009, 7, 17), 17.8], [dt.datetime(2009, 7, 18), 18.1],
        [dt.datetime(2009, 7, 19), 17.2], [dt.datetime(2009, 7, 20), 14.4],
        [dt.datetime(2009, 7, 21), 13.7], [dt.datetime(2009, 7, 22), 15.7], [dt.datetime(2009, 7, 23), 14.6],
        [dt.datetime(2009, 7, 24), 15.3], [dt.datetime(2009, 7, 25), 15.3], [dt.datetime(2009, 7, 26), 15.8],
        [dt.datetime(2009, 7, 27), 15.2], [dt.datetime(2009, 7, 28), 14.8], [dt.datetime(2009, 7, 29), 14.4],
        [dt.datetime(2009, 7, 30), 15], [dt.datetime(2009, 7, 31), 13.6]
    ]

    ranges = [
        [dt.datetime(2009, 7, 1), 14.3, 27.7], [dt.datetime(2009, 7, 2), 14.5, 27.8], [dt.datetime(2009, 7, 3), 15.5, 29.6],
        [dt.datetime(2009, 7, 4), 16.7, 30.7], [dt.datetime(2009, 7, 5), 16.5, 25.0], [dt.datetime(2009, 7, 6), 17.8, 25.7],
        [dt.datetime(2009, 7, 7), 13.5, 24.8], [dt.datetime(2009, 7, 8), 10.5, 21.4], [dt.datetime(2009, 7, 9), 9.2, 23.8],
        [dt.datetime(2009, 7, 10), 11.6, 21.8], [dt.datetime(2009, 7, 11), 10.7, 23.7], [dt.datetime(2009, 7, 12), 11.0, 23.3],
        [dt.datetime(2009, 7, 13), 11.6, 23.7], [dt.datetime(2009, 7, 14), 11.8, 20.7], [dt.datetime(2009, 7, 15), 12.6, 22.4],
        [dt.datetime(2009, 7, 16), 13.6, 19.6], [dt.datetime(2009, 7, 17), 11.4, 22.6], [dt.datetime(2009, 7, 18), 13.2, 25.0],
        [dt.datetime(2009, 7, 19), 14.2, 21.6], [dt.datetime(2009, 7, 20), 13.1, 17.1], [dt.datetime(2009, 7, 21), 12.2, 15.5],
        [dt.datetime(2009, 7, 22), 12.0, 20.8], [dt.datetime(2009, 7, 23), 12.0, 17.1], [dt.datetime(2009, 7, 24), 12.7, 18.3],
        [dt.datetime(2009, 7, 25), 12.4, 19.4], [dt.datetime(2009, 7, 26), 12.6, 19.9], [dt.datetime(2009, 7, 27), 11.9, 20.2],
        [dt.datetime(2009, 7, 28), 11.0, 19.3], [dt.datetime(2009, 7, 29), 10.8, 17.8], [dt.datetime(2009, 7, 30), 11.8, 18.5],
        [dt.datetime(2009, 7, 31), 10.8, 16.1]
    ]
    # Area Range plot
    area_range_plot = AreaRange(
        width='500px',
        height='500px',
        engine='highcharts',
        title='July Temperatures',
        y_axis_title='Temperature',
        y_axis_units='*C',
        series=[{
            'name': 'Temperature',
            'data': averages,
            'zIndex': 1,
            'marker': {
                'lineWidth': 2,
            }
        }, {
            'name': 'Range',
            'data': ranges,
            'type': 'arearange',
            'lineWidth': 0,
            'linkedTo': ':previous',
            'fillOpacity': 0.3,
            'zIndex': 0
        }]
    )
    
    context = {
        'docs_endpoint': docs_endpoint,
        'line_plot_view': line_plot_view,
        'web_plot': web_plot,
        'timeseries_plot': timeseries_plot,
        'pie_plot_view': pie_plot_view,
        'bar_plot_view': bar_plot_view,
        'area_range_plot': area_range_plot,
        'scatter_plot_view': scatter_plot_view,
        'd3_pie_plot_view': d3_pie_plot_view,
        'd3_line_plot_view': d3_line_plot_view,
        'd3_scatter_plot_view': d3_scatter_plot_view,
        'd3_bar_plot_view': d3_bar_plot_view,
        'd3_timeseries_plot_view': d3_timeseries_plot_view,
    }
    return render(request, 'gizmo_showcase/plot_view.html', context)


@login_required()
def plotly_view(request):
    """
    Controller for the Plotly View page.
    """
    x = [dt.datetime(year=2013, month=10, day=4),
         dt.datetime(year=2013, month=11, day=5),
         dt.datetime(year=2013, month=12, day=6)]

    my_plotly_view = PlotlyView([go.Scatter(x=x, y=[1, 3, 6])])
    context = {
        'docs_endpoint': docs_endpoint,
        'my_plotly_view': my_plotly_view,
    }
    return render(request, 'gizmo_showcase/plotly_view.html', context)


@login_required()
def bokeh_view(request):
    """
    Controller for the Bokeh View page.
    """
    plot = bokeh_figure(plot_height=300)
    plot.circle([1, 2], [3, 4])
    my_bokeh_view = BokehView(plot, height="300px")
    context = {
        'docs_endpoint': docs_endpoint,
        'my_bokeh_view': my_bokeh_view,
    }
    return render(request, 'gizmo_showcase/bokeh_view.html', context)
