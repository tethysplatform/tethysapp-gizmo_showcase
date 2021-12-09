from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def table_view(request):
    """
    Controller for the Table View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/table_view.html', context)


@login_required()
def datatable_view(request):
    """
    Controller for the DataTable View page.
    """
    context = {}
    return render(request, 'gizmo_showcase/datatable_view.html', context)
