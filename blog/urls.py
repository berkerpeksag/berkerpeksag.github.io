from django.conf.urls import patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .feeds import LatestEntriesFeed
from .views import ArchiveListView, BlogDetailView, BlogListView


urlpatterns = patterns('',
    (r'^feed/$', LatestEntriesFeed()),
)

urlpatterns += patterns('blog.views',
    (r'^$', BlogListView.as_view()),
    (r'^archive/$', ArchiveListView.as_view()),
    (r'^(?P<slug>[a-z0-9-]+)/$', BlogDetailView.as_view()),
    (r'^blog/(?P<slug>[a-z0-9-]+)/$', BlogDetailView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
