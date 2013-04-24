from django.views.generic import DetailView, ListView

from blog.models import Post


class BlogListView(ListView):

    queryset = Post.objects.filter(status=True, archive=False)[:3]
    context_object_name = 'blogs'
    template_name = 'blog/index.html'


class ArchiveListView(BlogListView):

    post_filter = Post.objects.filter(status=True, archive=False)
    queryset = post_filter.values('slug', 'title', 'pub_date', 'body')
    template_name = 'blog/archive.html'


class BlogDetailView(DetailView):

    queryset = Post.objects.filter(status=True)
    context_object_name = 'blog'
    template_name = 'blog/detail.html'
