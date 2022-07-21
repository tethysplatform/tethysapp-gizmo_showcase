from ..app import GizmoShowcase as app
from tethys_apps.exceptions import TethysAppSettingNotAssigned

# Docs version
docs_endpoint = 'http://docs.tethysplatform.org/en/latest'


def get_geoserver_wms():
    """Try to get the GeoServer service from setting."""
    try:
        return app.get_spatial_dataset_service('primary_geoserver', as_wms=True)
    except TethysAppSettingNotAssigned:
        return None
