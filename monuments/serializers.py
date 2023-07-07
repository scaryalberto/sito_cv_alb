# posts / serializers.py
from rest_framework import serializers
from .models import *


class MonumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monuments
        fields = '__all__'
