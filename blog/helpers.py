from django.shortcuts import render_to_response
from django.template import RequestContext


def render(template, params, request):
    return render_to_response('{0:s}.html'.format(template),
                              params,
                              context_instance=RequestContext(request))
