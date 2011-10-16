from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('blog.views',
    (r'^$', 'index'),
    (r'^(?P<slug>[a-z-]+)/$', 'detail'),
    (r'^(?P<slug>[a-z-]+)/comment/$', 'comment'),
)

urlpatterns += staticfiles_urlpatterns()