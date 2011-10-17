from blog.models import Post
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
    latest_blog_list = Post.objects.filter(status=True, archive=False)[:5]
    return render_to_response('blog/index.html', {'latest_blog_list': latest_blog_list})

def detail(request, slug):
    blog = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/detail.html', {'blog': blog})

def archive(request):
    archive_list = Post.objects.filter(status=1)
    return render_to_response('blog/archive.html', {'archive_list': archive_list})