from django.shortcuts import render
from .models import BlogArticles
# Create your views here.

def home_page(request):
    return render(request, 'cv/index.html', {})

def blog_posts(request):
    posts = BlogArticles.objects.all()
    print(posts)
    return render(request, 'cv/blog_posts.html', {'posts': posts})

def article(request):
    return render(request, 'cv/article.html', {})