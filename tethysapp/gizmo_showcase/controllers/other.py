from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import MessageBox
from .common import docs_endpoint


@login_required()
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
