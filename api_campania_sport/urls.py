from django.urls import path

from .views import *
urlpatterns= [
    path('campaniasport/', ArticleView.as_view()),
    path('monument/', MonumentView.as_view())#api per app monumenti
]
