from django.shortcuts import render
from tethys_sdk.gizmos import ESRIMap, EMLayer, EMView
from tethys_sdk.base import controller
from .common import docs_endpoint


@controller
def esri_map_view(request):
    """
    Controller for the Esri Map View page.
    """
    # Set initial view
    esri_map_view = EMView(
        center=[-100, 40], 
        zoom=4
    )
    
    # Define layers
    esri_layer = EMLayer(
        type='FeatureLayer',
        url='https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/USA_States_Generalized/FeatureServer'
    )

    vector_tile = EMLayer(
        type='ImageryLayer',
        url='https://sampleserver6.arcgisonline.com/arcgis/rest/services/NLCDLandCover2001/ImageServer'
    )

    esri_map = ESRIMap(
        height='700px', 
        width='100%', 
        basemap='topo-vector',
        view=esri_map_view, 
        layers=[vector_tile, esri_layer]
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'esri_map': esri_map
    }

    return render(request, 'gizmo_showcase/esri_map_view.html', context)
