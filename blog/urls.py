from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^archive/$', 'archive'),
    (r'^(?P<slug>[a-z-]+)/$', 'detail'),
)

urlpatterns += staticfiles_urlpatterns()