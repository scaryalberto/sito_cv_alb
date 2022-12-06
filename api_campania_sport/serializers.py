# posts / serializers.py
from rest_framework import serializers
from .models import CampaniaSportArticles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaniaSportArticles
        fields = '__all__'