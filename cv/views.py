from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import BlogArticles
from .forms import NewArticleForm

def home_page(request):
    return render(request, 'cv/index.html', {})



def blog_posts(request):
    posts = BlogArticles.objects.all()
    print(posts)
    return render(request, 'cv/blog_posts.html', {'posts': posts})


def article(request, id):
    post = get_object_or_404(BlogArticles, pk=id)
    return render(request, 'cv/article.html', {'post': post})

from django.shortcuts import redirect

@login_required
def add_article(request):
    context = {}

    # create object of form
    form = NewArticleForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        form.save()
        response = redirect('/blog_posts')
        return response

    context['form'] = form
    return render(request, "cv/new_article_form.html", context)