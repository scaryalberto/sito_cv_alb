from django.urls import path

from monuments.views import MonumentsView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("caserta/", MonumentsView.as_view(), name="caserta"),  # mi serve per creare i voli

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
