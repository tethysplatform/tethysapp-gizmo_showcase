from django.shortcuts import render
from tethys_sdk.routing import controller
from tethys_sdk.gizmos import Button, ButtonGroup, DatePicker, RangeSlider, \
    SelectInput, TextInput, ToggleSwitch
from .common import docs_endpoint


@controller
def buttons(request):
    """
    Controller for the Buttons page.
    """
    # Single button
    single_button = Button(
        display_text='Click Me',
        name='click_me_name',
        icon='menu-up',
        attributes='onclick=alert(this.name);',
        submit=True
    )

    # Horizontal Button Group
    add_button = Button(
        display_text='Add',
        icon='plus-circle-fill',
        style='outline-success',
        classes='btn-lg'
    )
    delete_button = Button(
        display_text='Delete',
        icon='trash2-fill',
        disabled=True,
        style='outline-danger',
        classes='btn-lg'
    )
    horizontal_buttons = ButtonGroup(
        buttons=[add_button, delete_button]
    )

    # Vertical Button Group
    edit_button = Button(
        display_text='Edit',
        icon='tools',
        style='warning',
        attributes='id="edit button" new_attr=attr'
    )
    info_button = Button(
        display_text='Info',
        icon='info-circle',
        style='info',
        attributes='name=info'
    )
    apps_button = Button(
        display_text='Apps',
        icon='app',
        href='/apps',
        style='primary'
    )
    vertical_buttons = ButtonGroup(
        buttons=[edit_button, info_button, apps_button],
        vertical=True
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'single_button': single_button,
        'horizontal_buttons': horizontal_buttons,
        'vertical_buttons': vertical_buttons,
    }
    return render(request, 'gizmo_showcase/buttons.html', context)


@controller
def date_picker(request):
    """
    Controller for the Date Picker page.
    """
    # Date Picker Options
    date_picker = DatePicker(
        name='date1',
        display_text='Date',
        autoclose=True,
        format='MM d, yyyy',
        start_date='2/15/2014',
        start_view='decade',
        today_button=True,
        initial='February 15, 2014'
    )

    date_picker_error = DatePicker(
        name='data2',
        display_text='Date',
        initial='10/2/2013',
        disabled=True,
        error='Here is my error text.'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'date_picker': date_picker,
        'date_picker_error': date_picker_error,
    }
    return render(request, 'gizmo_showcase/date_picker.html', context)


@controller
def range_slider(request):
    """
    Controller for the Range Slider page.
    """
    # Range Slider Data
    slider1 = RangeSlider(
        display_text='Slider 1',
        name='slider1',
        min=0,
        max=100,
        initial=50,
        step=1
    )
    slider2 = RangeSlider(
        display_text='Slider 2',
        name='slider2',
        min=0,
        max=1,
        initial=0.5,
        step=0.1,
        disabled=True,
        error='Incorrect, please choose another value.'
    )
    slider3 = RangeSlider(
        display_text='Slider 3',
        name='slider3',
        min=0,
        max=10,
        initial=5,
        step=1,
        success='Excellent choice!'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'slider1': slider1,
        'slider2': slider2,
        'slider3': slider3,
    }
    return render(request, 'gizmo_showcase/range_slider.html', context)


@controller
def select_input(request):
    """
    Controller for the Select Input page.
    """
    # Select2 Input
    select_input2 = SelectInput(
        display_text='Select2',
        name='select21',
        multiple=False,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['Three'],
        select2_options={'placeholder': 'Select a number',
                            'allowClear': True}
    )

    select_input2_multiple = SelectInput(
        display_text='Select2 Multiple',
        name='select22',
        multiple=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['Two', 'One']
    )

    select_input2_disabled = SelectInput(
        display_text='Select2 Disabled',
        name='select23',
        multiple=False,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        disabled=True,
    )
    
    select_input2_success = SelectInput(
        display_text='Select2 with Success',
        name='select24',
        multiple=False,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        success="Couldn't have chosen a better option."
    )
    
    select_input2_error = SelectInput(
        display_text='Select2 with Error',
        name='select25',
        multiple=False,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        error="Oops, don't pick that one."
    )

    # Select Classic
    select_input = SelectInput(
        display_text='Select',
        name='select1',
        multiple=False,
        original=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['Three']
    )
    
    select_input_disabled = SelectInput(
        display_text='Select Disabled',
        name='select1',
        multiple=False,
        original=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['1'],
        disabled=True
    )

    select_input_multiple = SelectInput(
        display_text='Select Multiple',
        name='select11',
        multiple=True,
        original=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')]
    )
    
    select_input_error = SelectInput(
        display_text='Select with Error',
        name='select1',
        multiple=False,
        original=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['Two'],
        error="That's an error, Jim."
    )
    
    select_input_success = SelectInput(
        display_text='Select with Success',
        name='select1',
        multiple=False,
        original=True,
        options=[('One', '1'), ('Two', '2'), ('Three', '3')],
        initial=['3'],
        success="Great choice!"
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'select_input2': select_input2,
        'select_input2_disabled': select_input2_disabled,
        'select_input2_multiple': select_input2_multiple,
        'select_input2_error': select_input2_error,
        'select_input2_success': select_input2_success,
        'select_input': select_input,
        'select_input_disabled': select_input_disabled,
        'select_input_multiple': select_input_multiple,
        'select_input_error': select_input_error,
        'select_input_success': select_input_success,
    }
    return render(request, 'gizmo_showcase/select_input.html', context)


@controller
def text_input(request):
    """
    Controller for the Text Input page.
    """
    # Text Input
    text_input = TextInput(
        display_text='Text',
        name='inputAmount',
        placeholder='e.g.: 10.00',
        prepend='$',
        append='/unit'
    )

    text_error_input = TextInput(
        display_text='Text Error',
        name='inputEmail',
        initial='bob@example.com',
        disabled=True,
        icon_append='envelope',
        error='Here is my error text'
    )
    
    text_success_input = TextInput(
        display_text='Text Error',
        name='inputName',
        initial='bob@example.com',
        icon_prepend='person',
        success='Good job!'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'text_input': text_input,
        'text_error_input': text_error_input,
        'text_success_input': text_success_input,
    }
    return render(request, 'gizmo_showcase/text_input.html', context)


@controller
def toggle_switch(request):
    """
    Controller for the Toggle Switch page.
    """
    # Toggle Switch
    toggle_switch = ToggleSwitch(
        display_text='Defualt Toggle',
        name='toggle1'
    )

    toggle_switch_styled = ToggleSwitch(
        display_text='Styled Toggle',
        name='toggle2',
        on_label='Yes',
        off_label='No',
        on_style='success',
        off_style='danger',
        initial=True,
        size='large'
    )
    
    toggle_switch_disabled = ToggleSwitch(
        display_text='Disabled Toggle',
        name='toggle2',
        on_label='Yes',
        off_label='No',
        on_style='success',
        off_style='danger',
        initial=True,
        disabled=True,
    )

    toggle_switch_error = ToggleSwitch(
        display_text='Error Toggle',
        name='toggle3',
        on_label='On',
        off_label='Off',
        on_style='success',
        off_style='warning',
        size='mini',
        initial=False,
        error='Here is my error text'
    )
    
    toggle_switch_success = ToggleSwitch(
        display_text='Success Toggle',
        name='toggle3',
        on_label='On',
        off_label='Off',
        on_style='primary',
        off_style='danger',
        initial=True,
        success='Here is my success text'
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'toggle_switch': toggle_switch,
        'toggle_switch_styled': toggle_switch_styled,
        'toggle_switch_disabled': toggle_switch_disabled,
        'toggle_switch_success': toggle_switch_success,
        'toggle_switch_error': toggle_switch_error,
    }
    return render(request, 'gizmo_showcase/toggle_switch.html', context)
