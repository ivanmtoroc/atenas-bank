# Django Rest Framework
from rest_framework import serializers

# Models
from backend.apps.tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
