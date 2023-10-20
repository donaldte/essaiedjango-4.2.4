from django import template

register = template.Library()

@register.filter(name='upper_case')
def upper_case(value):
    return value.upper()


@register.filter(name='lower_case')
def lower_case(value):
    return value.lower()


@register.filter(name='multiply')
def multiply(value, arg):
    return value * arg