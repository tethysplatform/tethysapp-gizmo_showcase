from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def plot_view(request):
    """
    Controller for the Plot View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/plot_view.html', context)


@login_required()
def plotly_view(request):
    """
    Controller for the Plotly View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/plotly_view.html', context)


@login_required()
def bokeh_view(request):
    """
    Controller for the Bokeh View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/bokeh_view.html', context)
