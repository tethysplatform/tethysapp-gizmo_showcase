from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import MessageBox, SlideSheet
from .common import docs_endpoint


@controller
def message_box(request):
    """
    Controller for the Message Box page.
    """
    # Message Box
    message_box = MessageBox(
        name='sampleModal',
        title='Message Box Title',
        message='Congratulations! This is a message box.',
        dismiss_button='Nevermind',
        affirmative_button='Proceed',
        width=400,
        affirmative_attributes='href=javascript:void(0);'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'message_box': message_box,
    }
    return render(request, 'gizmo_showcase/message_box.html', context)


@controller
def slide_sheet(request):
    """
    Controller for the Slide Sheet page.
    """
    slide_sheet = SlideSheet(
        id='plot-slide-sheet',
        title='Plot Slide Sheet',
        content_template='gizmo_showcase/slide_sheet_content.html'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'slide_sheet': slide_sheet,
    }
    return render(request, 'gizmo_showcase/slide_sheet.html', context)
