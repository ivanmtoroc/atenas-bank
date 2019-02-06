# Django Rest Framework
from rest_framework import serializers

# Models
from apps.offices.models import Office

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'
