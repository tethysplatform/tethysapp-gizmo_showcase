from django.shortcuts import render
from tethys_sdk.gizmos import TableView, DataTableView
from tethys_sdk.base import controller
from .common import docs_endpoint


@controller
def table_view(request):
    """
    Controller for the Table View page.
    """
    table_view = TableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
                ('Fred', 18, 'programmer'),
                ('Bob', 26, 'boss')],
        hover=True,
        striped=False,
        bordered=False,
        condensed=False
    )
    
    dark_table_view = TableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
                ('Fred', 18, 'programmer'),
                ('Bob', 26, 'boss')],
        hover=True,
        striped=True,
        bordered=True,
        condensed=False,
        dark=True
    )

    table_view_edit = TableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
                ('Fred', 18, 'programmer'),
                ('Bob', 26, 'boss')],
        hover=True,
        striped=True,
        bordered=False,
        condensed=False,
        editable_columns=(False, 'ageInput', 'jobInput'),
        row_ids=[21, 25, 31]
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'table_view': table_view,
        'dark_table_view': dark_table_view,
        'table_view_edit': table_view_edit,
    }
    return render(request, 'gizmo_showcase/table_view.html', context)


@controller
def datatable_view(request):
    """
    Controller for the DataTable View page.
    """
    datatable_default = DataTableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
            ('Fred', 18, 'programmer'),
            ('Bob', 26, 'boss')],
        searching=False,
        orderClasses=False,
        lengthMenu=[[10, 25, 50, -1], [10, 25, 50, "All"]],
    )
    
    datatable_dark = DataTableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
            ('Fred', 18, 'programmer'),
            ('Bob', 26, 'boss')],
        searching=False,
        orderClasses=False,
        lengthMenu=[[10, 25, 50, -1], [10, 25, 50, "All"]],
        hover=True,
        striped=True,
        dark=True,
    )

    datatable_with_extension = DataTableView(
        column_names=('Name', 'Age', 'Job'),
        rows=[('Bill', 30, 'contractor'),
            ('Fred', 18, 'programmer'),
            ('Bob', 26, 'boss')],
        colReorder=True,
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'datatable_default': datatable_default,
        'datatable_dark': datatable_dark,
        'datatable_with_extension': datatable_with_extension,
    }
    return render(request, 'gizmo_showcase/datatable_view.html', context)
