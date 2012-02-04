from django import template
register = template.Library()

@register.filter
def inlist(value,arg):
    # Checks if the value is in the list
    return value in arg
