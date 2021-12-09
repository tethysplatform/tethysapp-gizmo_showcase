from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def jobs_table(request):
    """
    Controller for the Jobs Table page.
    """
    context = {}
    return render(request, 'gizmo_showcase/jobs_table.html', context)
