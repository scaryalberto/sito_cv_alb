"""sito_cv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('swagger/', schema_view),
    path('admin/', admin.site.urls),
    path('', include('cv.urls')),
    path("accounts/", include("django.contrib.auth.urls")), #necessario per creare la pagina di login
    path('api/', include('api_campania_sport.urls')), #http://127.0.0.1:8000/api/campaniasport/
    path('fleet_flights/', include('aviation_management_system.urls')), #http://127.0.0.1:8000/fleet_flights/made_flights/

]


