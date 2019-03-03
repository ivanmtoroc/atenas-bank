# Django Rest Framework
from rest_framework import serializers

# Models
from apps.ads.models import Ad


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
