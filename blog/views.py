from django.conf import settings
from django.shortcuts import get_object_or_404
from django.views.decorators.http import last_modified

from blog.decorators import render
from blog.models import Post


def last_update_date(request, **kwargs):
    if not settings.USE_ETAGS:
        return None
    post = Post.objects
    if kwargs.get('slug'):
        update_date = post.get(slug=kwargs['slug']).update_date
    else:
        update_date = post.latest('update_date').update_date
    return update_date


@last_modified(last_update_date)
@render('blog/index')
def index(request):
    blogs = Post.objects.filter(status=True, archive=False)[:3]
    return {'blogs': blogs}


@last_modified(last_update_date)
@render('blog/detail')
def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return {'blog': blog}


@last_modified(last_update_date)
@render('blog/archive')
def archive(request):
    blogs = Post.objects.filter(status=True, archive=False) \
                        .values('slug', 'title', 'pub_date', 'body')
    return {'blogs': blogs}
