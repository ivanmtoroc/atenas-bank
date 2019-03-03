# Django Rest Framework
from rest_framework import serializers

# Models
from apps.clients.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
