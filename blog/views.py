from blog.models import Post
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
import datetime


def index(request):
    latest_blog_list = Post.objects.filter(status=1)[:5]
    return render_to_response('blog/index.html', {'latest_blog_list': latest_blog_list})

def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/detail.html', {'blog': blog}, context_instance=RequestContext(request))

def comment(request, slug):
    blog = get_object_or_404(Post, slug=slug)

    blog.comment_set.create(author=request.POST['author'], email=request.POST['email'], body=request.POST['body'], ip='127.0.0.1', pub_date=datetime.datetime.now())
    blog.save()

    return HttpResponseRedirect(reverse('blog.views.detail', args=(blog.slug,)))