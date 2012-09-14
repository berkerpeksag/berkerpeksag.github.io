from blog.helpers import render
from blog.models import Post
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def index(request):
    latest_blog_list = Post.objects.filter(status=True, archive=False)[:5]
    return render('blog/index', {'latest_blog_list': latest_blog_list}, request)


def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render('blog/detail', {'blog': blog}, request)


def archive(request):
    archive_list = Post.objects.filter(status=True, archive=False).values('slug', 'title', 'pub_date')
    return render('blog/archive', {'archive_list': archive_list}, request)
