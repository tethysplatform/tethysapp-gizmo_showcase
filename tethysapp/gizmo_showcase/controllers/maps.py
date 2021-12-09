from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def map_view(request):
    """
    Controller for the Map View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/map_view.html', context)


@login_required()
def esri_map_view(request):
    """
    Controller for the Esri Map View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/esri_map_view.html', context)


@login_required()
def cesium_map_view(request):
    """
    Controller for the Cesium Map View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/cesium_map_view.html', context)
