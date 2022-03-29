from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def posts(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao') 
    return render(request, 'posts/posts.html', {'posts': posts})

def detalhe_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/detalhe_post.html', {'post': post})