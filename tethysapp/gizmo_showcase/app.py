from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting

from tethys_sdk.app_settings import SpatialDatasetServiceSetting


class GizmoShowcase(TethysAppBase):
    """
    Tethys app class for Gizmo Showcase.
    """

    name = 'Gizmo Showcase'
    index = 'home'
    icon = 'gizmo_showcase/images/gizmos.png'
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

    def spatial_dataset_service_settings(self):
        """
        Example spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='primary_geoserver',
                description='Optional GeoServer service used for map gizmo demos.',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=False,
            ),
        )

        return sds_settings
