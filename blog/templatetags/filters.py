from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def splitfirst(string):
    return string.split('\n')[0]
