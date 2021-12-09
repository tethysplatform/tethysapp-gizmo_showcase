from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import ESRIMap, EMLayer, EMView
from .common import docs_endpoint


@login_required()
def esri_map_view(request):
    """
    Controller for the Esri Map View page.
    """
    esri_map_view = EMView(center=[-100, 40], zoom=4)
    esri_layer = EMLayer(
        type='FeatureLayer',
        url='http://geoserver.byu.edu/arcgis/rest/services/gaugeviewer/AHPS_gauges/MapServer/0'
    )

    vector_tile = EMLayer(
        type='ImageryLayer',
        url='https://sampleserver6.arcgisonline.com/arcgis/rest/services/NLCDLandCover2001/ImageServer'
    )

    esri_map = ESRIMap(height='400px', width='100%', basemap='topo',
                       view=esri_map_view, layers=[vector_tile, esri_layer])

    context = {
        'docs_endpoint': docs_endpoint,
        'esri_map': esri_map
    }

    return render(request, 'gizmo_showcase/esri_map_view.html', context)
