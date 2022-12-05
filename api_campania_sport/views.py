from rest_framework import viewsets

from .models import CampaniaSportArticles, Monuments
from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
import json

class ArticleView(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = CampaniaSportArticles.objects.all()
            print(queryset)

            queryset = serializers.serialize("json", CampaniaSportArticles.objects.all())
            queryset = json.loads(queryset)

            return Response(queryset)

class Monumenti(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = Monuments.objects.all()
            print(queryset)

            queryset = serializers.serialize("json", Monuments.objects.all())
            queryset = json.loads(queryset)

            return Response(queryset)