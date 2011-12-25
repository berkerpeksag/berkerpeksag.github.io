from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('blog.urls')),
)

urlpatterns += staticfiles_urlpatterns()
