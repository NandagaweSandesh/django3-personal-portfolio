from django.shortcuts import render, get_object_or_404
from .models import Blog

app_name = 'blog'

def all_blogs(request):
    blog = Blog.objects.all() [:3]
    return render(request, 'blog/all_blogs.html', {'blogs':blog})


def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
