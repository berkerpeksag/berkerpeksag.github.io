from django.conf.urls import include, patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

admin.autodiscover()

ADMIN_URL = 'https://docs.djangoproject.com/en/dev/ref/contrib/admin/'

urlpatterns = patterns('',
    (r'^nimda/', include(admin.site.urls)),
    (r'^admin/$', RedirectView.as_view(url=ADMIN_URL)),
    (r'^', include('blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()
