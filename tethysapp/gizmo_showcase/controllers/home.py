from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def home(request):
    """
    Controller for the Quick Start (home) page.
    """
    context = {}
    return render(request, 'gizmo_showcase/home.html', context)
