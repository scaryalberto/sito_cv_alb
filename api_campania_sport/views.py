from rest_framework import viewsets

from .models import Articles, Monuments
from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
import json

class ArticleView(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = Articles.objects.all()
            print(queryset)

            queryset = serializers.serialize("json", Articles.objects.all())
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