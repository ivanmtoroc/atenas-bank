# Rest Framework
from rest_framework import serializers

# Clients models
from apps.clients.models import ClientModel

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
