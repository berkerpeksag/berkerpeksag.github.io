from django.contrib.syndication.views import Feed
from blog.models import Post


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

    def item_description(self, item):
        return item.body
