from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button


@login_required()
def buttons(request):
    """
    Controller for the Buttons page.
    """
    context = {}
    return render(request, 'gizmo_showcase/buttons.html', context)


@login_required()
def date_picker(request):
    """
    Controller for the Date Picker page.
    """
    context = {}
    return render(request, 'gizmo_showcase/date_picker.html', context)


@login_required()
def range_slider(request):
    """
    Controller for the Range Slider page.
    """
    context = {}
    return render(request, 'gizmo_showcase/range_slider.html', context)


@login_required()
def select_input(request):
    """
    Controller for the Select Input page.
    """
    context = {}
    return render(request, 'gizmo_showcase/select_input.html', context)


@login_required()
def text_input(request):
    """
    Controller for the Text Input page.
    """
    context = {}
    return render(request, 'gizmo_showcase/text_input.html', context)


@login_required()
def toggle_switch(request):
    """
    Controller for the Toggle Switch page.
    """
    context = {}
    return render(request, 'gizmo_showcase/toggle_switch.html', context)
