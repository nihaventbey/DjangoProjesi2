from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import StaticPage


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # veya neye göre sıralamak istiyorsan
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def static_page(request, slug):
    page = get_object_or_404(StaticPage, slug=slug, is_published=True)
    return render(request, 'blog/static_page.html', {'page': page})
