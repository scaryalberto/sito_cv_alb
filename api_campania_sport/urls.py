from django.urls import path

from .views import *
urlpatterns= [
    path('campaniasport/', ArticleView.as_view())
]
