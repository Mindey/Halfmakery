from django import template

register = template.Library()

@register.simple_tag
def coin(satoshis):
    return float(satoshis)/100000000
