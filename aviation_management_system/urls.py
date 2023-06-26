from django.urls import path

from . import views
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import FlightsView, mappa

urlpatterns = [
      path("made_flights/", FlightsView.as_view(), name="blog_posts"), #mi serve per creare i voli
      path("map_flights/", mappa, name="blog_posts"),  # mi serve per creare i voli

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
