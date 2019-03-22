# Django Rest Framework
from rest_framework import serializers

# Models
from apps.tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
