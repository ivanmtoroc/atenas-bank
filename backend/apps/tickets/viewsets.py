# Django Rest Framework
from rest_framework.response import Response
from rest_framework import viewsets

# Serializers
from apps.tickets.serializers import TicketSerializer

# Models
from apps.tickets.models import Ticket


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def destroy(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket.is_active = not ticket.is_active
        ticket.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)
