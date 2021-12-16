from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class GizmoShowcase(TethysAppBase):
    """
    Tethys app class for Gizmo Showcase.
    """

    name = 'Gizmo Showcase'
    index = 'gizmo_showcase:home'
    icon = 'gizmo_showcase/images/icon.gif'
    package = 'gizmo_showcase'
    root_url = 'gizmo-showcase'
    color = '#2c3e50'
    description = 'An app with explanations and demonstrations of each of the Tethys Gizmos.'
    tags = ''
    enable_feedback = False
    feedback_emails = []
    
    def custom_settings(self):
        """
        Define custom settings for the app.
        """
        custom_settings = (
            CustomSetting(
                name='cesium_ion_token',
                type=CustomSetting.TYPE_STRING,
                description='CesiumIon Token for the CesiumMapView examples.',
                required=True,
            ),
        )
        return custom_settings

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='gizmo-showcase',
                controller='gizmo_showcase.controllers.home.home'
            ),
            UrlMap(
                name='buttons',
                url='gizmo-showcase/buttons',
                controller='gizmo_showcase.controllers.form_controls.buttons'
            ),
            UrlMap(
                name='date_picker',
                url='gizmo-showcase/date-picker',
                controller='gizmo_showcase.controllers.form_controls.date_picker'
            ),
            UrlMap(
                name='range_slider',
                url='gizmo-showcase/range-slider',
                controller='gizmo_showcase.controllers.form_controls.range_slider'
            ),
            UrlMap(
                name='select_input',
                url='gizmo-showcase/select-input',
                controller='gizmo_showcase.controllers.form_controls.select_input'
            ),
            UrlMap(
                name='text_input',
                url='gizmo-showcase/text-input',
                controller='gizmo_showcase.controllers.form_controls.text_input'
            ),
            UrlMap(
                name='toggle_switch',
                url='gizmo-showcase/toggle-switch',
                controller='gizmo_showcase.controllers.form_controls.toggle_switch'
            ),
            UrlMap(
                name='table_view',
                url='gizmo-showcase/table-view',
                controller='gizmo_showcase.controllers.tables.table_view'
            ),
            UrlMap(
                name='datatable_view',
                url='gizmo-showcase/datatable-view',
                controller='gizmo_showcase.controllers.tables.datatable_view'
            ),
            UrlMap(
                name='plot_view_highcharts',
                url='gizmo-showcase/plot-view-hc',
                controller='gizmo_showcase.controllers.plots.plot_view_highcharts'
            ),
            UrlMap(
                name='plot_view_d3',
                url='gizmo-showcase/plot-view-d3',
                controller='gizmo_showcase.controllers.plots.plot_view_d3'
            ),
            UrlMap(
                name='plotly_view',
                url='gizmo-showcase/plotly-view',
                controller='gizmo_showcase.controllers.plotly.plotly_view'
            ),
            UrlMap(
                name='bokeh_view',
                url='gizmo-showcase/bokeh-view',
                controller='gizmo_showcase.controllers.bokeh.bokeh_view'
            ),
            UrlMap(
                name='map_view',
                url='gizmo-showcase/map-view',
                controller='gizmo_showcase.controllers.map_view.map_view'
            ),
            UrlMap(
                name='esri_map_view',
                url='gizmo-showcase/esri-map-view',
                controller='gizmo_showcase.controllers.esri_map_view.esri_map_view'
            ),
            UrlMap(
                name='cesium_map_view_basic',
                url='gizmo-showcase/cesium-map-view',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_basic'
            ),
            UrlMap(
                name='cesium_map_view_layers',
                url='gizmo-showcase/cesium-map-view-layers',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_layers'
            ),
            UrlMap(
                name='cesium_map_view_terrain',
                url='gizmo-showcase/cesium-map-view-terrain',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_terrain'
            ),
            UrlMap(
                name='cesium_map_view_czml',
                url='gizmo-showcase/cesium-map-view-czml',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_czml'
            ),
            UrlMap(
                name='cesium_map_view_geojson',
                url='gizmo-showcase/cesium-map-view-geojson',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_geojson'
            ),
            UrlMap(
                name='cesium_map_view_model',
                url='gizmo-showcase/cesium-map-view-model',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_model'
            ),
            UrlMap(
                name='cesium_map_view_multi_model',
                url='gizmo-showcase/cesium-map-view-multi-model',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_multi_model'
            ),
            UrlMap(
                name='cesium_map_view_draw',
                url='gizmo-showcase/cesium-map-view-multi-draw',
                controller='gizmo_showcase.controllers.cesium_map_view.cesium_map_view_draw'
            ),
            UrlMap(
                name='jobs_table',
                url='gizmo-showcase/jobs-table',
                controller='gizmo_showcase.controllers.processing.jobs_table'
            ),
            UrlMap(
                name='jobs_table_results',
                url='gizmo-showcase/jobs-table/{job_id}/results',
                controller='gizmo_showcase.controllers.processing.jobs_table_results'
            ),
            UrlMap(
                name='jobs_table_sample_jobs',
                url='gizmo-showcase/jobs-table/sample-jobs',
                controller='gizmo_showcase.controllers.processing.create_sample_jobs'
            ),
            UrlMap(
                name='message_box',
                url='gizmo-showcase/message-box',
                controller='gizmo_showcase.controllers.other.message_box'
            ),
        )

        return url_maps