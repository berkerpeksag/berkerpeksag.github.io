def debug_mode(request):
    from django.conf import settings
    return dict(debug_mode=settings.DEBUG)
