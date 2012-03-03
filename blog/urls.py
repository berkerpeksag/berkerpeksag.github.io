from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.feeds import LatestEntriesFeed


urlpatterns = patterns('',
    (r'^feed/$', LatestEntriesFeed()),
)

urlpatterns += patterns('blog.views',
    (r'^$', 'index'),
    (r'^archive/$', 'archive'),
    (r'^(?P<slug>[a-z0-9-]+)/$', 'detail'),
    (r'^blog/(?P<slug>[a-z0-9-]+)/$', 'detail'),
)

urlpatterns += staticfiles_urlpatterns()
