from django.urls import path

from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("blog_posts/", views.blog_posts, name="blog_posts"),
    path("article/", views.article, name="article"),
    url(r'^(?P<id>\d+)/$', views.article)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)