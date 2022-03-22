from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import LinePlot, BarPlot, ScatterPlot, \
    PiePlot, TimeSeries, PolarPlot, AreaRange
from .common import docs_endpoint
from .data import air_temperature, water_temperature, male_dataset, female_dataset, \
    winter_time_series_08, winter_time_series_09, temperature_averages, temperature_ranges, \
    parameter_names, park_city_parameters, maple_dell_parameters, browser_share_hc, \
    browser_share_d3, months, year_1800, year_1900, year_2000, year_2008


@controller(
    url='gizmo-showcase/plot-view-hc'
)
def plot_view_highcharts(request):
    """
    Controller for the Plot View page.
    """
    # Line Plot
    line_plot_view = LinePlot(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Plot Title',
        subtitle='Plot Subtitle',
        spline=True,
        x_axis_title='Altitude',
        x_axis_units='km',
        y_axis_title='Temperature',
        y_axis_units='°C',
        series=[air_temperature, water_temperature]
    )

    # Scatter Plot
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

    # Polar Plot
    web_plot = PolarPlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Polar Chart',
        subtitle='Polar Chart',
        pane={
            'size': '80%'
        },
        categories=parameter_names,
        series=[park_city_parameters, maple_dell_parameters]
    )

    # Pie Plot
    pie_plot_view = PiePlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Pie Chart',
        subtitle='Pie Chart',
        series=[browser_share_hc]
    )

    # Bar Plot
    bar_plot_view = BarPlot(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Bar Chart',
        subtitle='Bar Chart',
        vertical=False,
        categories=months,
        axis_units='millions',
        axis_title='Population',
        series=[year_1800, year_1900, year_2000, year_2008]
    )

    # Time series plot
    time_series_plot = TimeSeries(
        width='500px',
        height='500px',
        engine='highcharts',
        title='Irregular Time series Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[winter_time_series_08, winter_time_series_09]
    )

    # Area Range plot
    area_range_plot = AreaRange(
        width='500px',
        height='500px',
        engine='highcharts',
        title='July Temperatures',
        y_axis_title='Temperature',
        y_axis_units='*C',
        series=[temperature_averages, temperature_ranges]
    )
    
    context = {
        'docs_endpoint': docs_endpoint,
        'line_plot_view': line_plot_view,
        'web_plot': web_plot,
        'time_series_plot': time_series_plot,
        'pie_plot_view': pie_plot_view,
        'bar_plot_view': bar_plot_view,
        'area_range_plot': area_range_plot,
        'scatter_plot_view': scatter_plot_view,
    }
    return render(request, 'gizmo_showcase/plot_view_hc.html', context)


@controller(
    url='gizmo-showcase/plot-view-d3'
)
def plot_view_d3(request):
    """
    Controller for the Plot View page.
    """
    # Line Plot
    d3_line_plot_view = LinePlot(
        height='500px',
        width='100%',
        engine='d3',
        title='Plot Title',
        subtitle='Plot Subtitle',
        spline=True,
        x_axis_title='Altitude',
        x_axis_units='km',
        y_axis_title='Temperature',
        y_axis_units='°C',
        series=[air_temperature, water_temperature]
    )

    # Scatter Plot
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

    # Pie Plot
    d3_pie_plot_view = PiePlot(
        width='100%',
        height='500px',
        engine='d3',
        title='Pie Chart',
        subtitle='Pie Chart',
        series=browser_share_d3
    )

    # Bar Plot
    d3_bar_plot_view = BarPlot(
        width='100%',
        title='Bar Chart',
        subtitle='Bar Chart',
        vertical=True,
        categories=months,
        axis_units='millions',
        axis_title='Population',
        series=[year_1800, year_1900, year_2000, year_2008]
    )

    # Time series plot
    d3_time_series_plot_view = TimeSeries(
        width='100%',
        title='Irregular Time series Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[winter_time_series_08, winter_time_series_09]
    )
    
    context = {
        'docs_endpoint': docs_endpoint,
        'd3_pie_plot_view': d3_pie_plot_view,
        'd3_line_plot_view': d3_line_plot_view,
        'd3_scatter_plot_view': d3_scatter_plot_view,
        'd3_bar_plot_view': d3_bar_plot_view,
        'd3_time_series_plot_view': d3_time_series_plot_view,
    }
    return render(request, 'gizmo_showcase/plot_view_d3.html', context)
