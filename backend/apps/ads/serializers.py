# Rest Framework
from rest_framework import serializers

# Ads models
from apps.ads.models import AdModel

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdModel
        fields = '__all__'
