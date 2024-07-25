from django.shortcuts import render , get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request):
  posts = Post.objects.all()
  return render(request, 'blog/post_list.html',{'posts':posts})
# Create your views here.

def post_detail(request, slug):
    post = get_object_or_404(Post , slug=slug , status=Post.Status.PUBLISHED)




    return render(request, 'blog/post_detail.html', {'post':post})
