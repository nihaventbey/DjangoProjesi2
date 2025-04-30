from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def index(request):
    return render(request, 'blog/index.html')
