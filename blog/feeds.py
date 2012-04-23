from django.contrib.syndication.views import Feed
from django.utils.safestring import mark_safe

from blog.models import Post

import markdown


def _markdown(value):
    return mark_safe(markdown.markdown(value))


class LatestEntriesFeed(Feed):

    def title(self):
        return 'Berker Peksag'

    def description(self):
        return 'Latest posts from berkerpeksag.com'

    def link(self):
        return '/'

    def feed_url(self):
        return '/feed/'

    def items(self):
        return Post.objects.order_by('-pub_date')[:5]

    def item_author_name(self):
        return 'Berker Peksag'

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.get_absolute_url()

    def item_description(self, item):
        return _markdown(item.body)
