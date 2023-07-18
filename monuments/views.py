import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from api_campania_sport.models import CampaniaSportArticles
from monuments.models import Monuments


def home_page(request):
    return render(request, 'cv/index.html', {})


class MonumentsView(APIView):
    """
    classe per le chiamate http
    """
    def get(self, request):
        if request.method == 'GET':

            messages = Monuments.objects.all()
            queryset_values = messages.values()  # Ottieni una lista di dizionari
            json_data = json.dumps(list(queryset_values))  # Converti in formato JSON
            return HttpResponse(json_data, content_type='application/json')
