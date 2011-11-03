from django import template

register = template.Library()

@register.simple_tag
def script(request, source, pattern):
    if not request.path.startswith(pattern):
        return '<script src="{:s}"></script>'.format(source)
    return ''