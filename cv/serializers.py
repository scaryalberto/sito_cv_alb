# posts / serializers.py
from rest_framework import serializers
from .models import *


class GftMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GftMessages
        fields = '__all__'
