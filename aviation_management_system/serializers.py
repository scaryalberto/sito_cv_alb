# posts / serializers.py
from rest_framework import serializers
from .models import *


class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'
