from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class GizmoShowcase(TethysAppBase):
    """
    Tethys app class for Gizmo Showcase.
    """

    name = 'Gizmo Showcase'
    description = 'An app with explanations and demonstrations of each of the Tethys Gizmos.'
    package = 'gizmo_showcase'  # WARNING: Do not change this value
    icon = f'{package}/images/icon.gif'
    root_url = 'gizmo-showcase'
    index = 'home'
    color = '#2c3e50'
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
