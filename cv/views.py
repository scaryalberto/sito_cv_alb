from django.shortcuts import render, get_object_or_404
from .models import BlogArticles
# Create your views here.

def home_page(request):
    return render(request, 'cv/index.html', {})

def blog_posts(request):
    posts = BlogArticles.objects.all()
    print(posts)
    return render(request, 'cv/blog_posts.html', {'posts': posts})


def article(request, id):
    post = get_object_or_404(BlogArticles, id=id)
    return render(request, 'cv/article.html', {'post':post})
