from django.utils.timesince import timesince as _timesince
from jingo import register
from markdown import markdown


@register.filter
def splitfirst(string):
    return string.splitlines()[0]


@register.function
def markup(string, extensions=None, split_first=False):
    if extensions is None:
        extensions = ['codehilite']
    else:
        extensions = [ext for ext in extensions.split(',') if ext]
    if 'safe' in extensions:
        extensions = extensions.remove('safe')
        options = {'safe_mode': True, 'enable_attributes': False}
    else:
        options = {'safe_mode': False}
    output = markdown(string, extensions, **options)
    if split_first:
        return splitfirst(output)
    return output


@register.filter
def timesince(string):
    if not string:
        return ''
    try:
        return _timesince(string)
    except (ValueError, TypeError):
        return ''
