import pandas as pd
import requests
from bs4 import BeautifulSoup
from api_campania_sport.models import CampaniaSportArticles
from .models import CampaniaSportArticles, Monuments
from django.core import serializers

from rest_framework.response import Response
from rest_framework.views import APIView
import json


class AlbertoBotView(APIView):
    def get(self, request):
        if request.method == 'GET':
            #todo: inserire le domande che posso fare ad Alberto ed eventualemte il gioco
            queryset = serializers.serialize("json", CampaniaSportArticles.objects.all())
            queryset = json.loads(queryset)

            from django.http import JsonResponse

            return JsonResponse({'all_campaniasport_articles': queryset})


class ArticleView(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = serializers.serialize("json", CampaniaSportArticles.objects.all())
            queryset = json.loads(queryset)

            from django.http import JsonResponse

            return JsonResponse({'all_campaniasport_articles': queryset})


def get_image_url(soup):
    soup_like_string = str(soup)
    image_url = soup_like_string.split('data-orig-file=')[1].split(' ')[0]
    return image_url.replace('"', '')

def change_date(date_article):
    from datetime import datetime

    date_article = date_article.split(' ')[1:]
    if date_article[1].lower() == 'gennaio':
        month = '1'
    elif date_article[1].lower() == 'febbraio':
        month = '2'
    elif date_article[1].lower() == 'marzo':
        month = '3'
    elif date_article[1].lower() == 'aprile':
        month = '4'
    elif date_article[1].lower() == 'maggio':
        month = '5'

    elif date_article[1].lower() == 'giugno':
        month = '6'

    elif date_article[1].lower() == 'luglio':
        month = '7'

    elif date_article[1].lower() == 'agosto':
        month = '8'

    elif date_article[1].lower() == 'settembre':
        month = '9'

    elif date_article[1].lower() == 'ottobre':
        month = '10'

    elif date_article[1].lower() == 'novembre':
        month = '11'

    elif date_article[1].lower() == 'dicembre':
        month = '12'

    datetime = datetime.strptime(date_article[2] + '-' + month + '-' + date_article[0], '%Y-%m-%d')
    print(datetime)

    return datetime


class Monumenti(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = Monuments.objects.all()
            print(queryset)

            queryset = serializers.serialize("json", Monuments.objects.all())
            queryset = json.loads(queryset)

            return Response(queryset)



def get_image_url(soup):
    soup_like_string=str(soup)
    image_url=soup_like_string.split('data-orig-file=')[1].split(' ')[0]
    return image_url.replace('"', '')



class MonumentView(APIView):
    def get(self, request):
        if request.method == 'GET':
            queryset = serializers.serialize("json", Monuments.objects.all())
            queryset = json.loads(queryset)

            from django.http import JsonResponse

            return JsonResponse({'all_monuments': queryset})
