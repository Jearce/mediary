from django import template
from copy import copy

register = template.Library()

@register.filter
def instances_and_widgets(bound_field):
    print(bound_field)
    '''
    https://stackoverflow.com/questions/4437386/how-to-loop-over-form-field-choices-and-display-associated-model-instance-fields
    '''

    instances_widgets = []
    index = 0
    for instance in bound_field.field.queryset.all():
        widget = copy(bound_field[index])
        instances_widgets.append((instance, widget))
        index += 1

    return instances_widgets
