from django.shortcuts import get_object_or_404

from blog.decorators import render
from blog.models import Post


@render('blog/index')
def index(request):
    blogs = Post.objects.filter(status=True, archive=False)[:5]
    return {'blogs': blogs}


@render('blog/detail')
def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return {'blog': blog}


@render('blog/archive')
def archive(request):
    archive = Post.objects.filter(status=True,
        archive=False).values('slug', 'title', 'pub_date')
    return {'archive': archive}
