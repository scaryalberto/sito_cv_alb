from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("blog_posts/", views.blog_posts, name="blog_posts"),
    path("article/", views.article, name="article"),

]