from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def message_box(request):
    """
    Controller for the Message Box page.
    """
    context = {}
    return render(request, 'gizmo_showcase/message_box.html', context)
