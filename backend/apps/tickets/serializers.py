# Rest Framework
from rest_framework import serializers

# Tickets models
from apps.tickets.models import TicketModel

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'
