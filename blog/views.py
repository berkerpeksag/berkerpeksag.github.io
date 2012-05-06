from blog.models import Post
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext


def index(request):
    latest_blog_list = Post.objects.filter(status=True, archive=False)[:3]
    return render_to_response('blog/index.html',
                              {'latest_blog_list': latest_blog_list},
                              context_instance=RequestContext(request))


def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/detail.html', {'blog': blog},
                              context_instance=RequestContext(request))


def archive(request):
    archive_list = Post.objects.filter(status=True, archive=False)
    archive_old_list = Post.objects.filter(status=True, archive=True)
    return render_to_response('blog/archive.html',
                              {'archive_list': archive_list,
                               'archive_old_list': archive_old_list},
                              context_instance=RequestContext(request))
