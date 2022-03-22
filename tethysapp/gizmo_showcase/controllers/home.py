from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button


@controller
def home(request):
    """
    Controller for the Quick Start (home) page.
    """
    context = {}
    return render(request, 'gizmo_showcase/home.html', context)
