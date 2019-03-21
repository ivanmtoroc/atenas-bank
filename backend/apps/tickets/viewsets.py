# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from apps.tickets.serializers import TicketSerializer

# Models
from apps.tickets.models import Ticket

# Python
from datetime import datetime, timedelta


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    # permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket.is_active = not ticket.is_active
        ticket.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)

    @action(detail = True, methods = ['get'])
    def init_attention(self, request, pk = None):
        ticket = self.get_object()
        ticket.init_time = datetime.now()
        ticket.status = 'IAT'
        ticket.save()
        data = {
            'message': 'Time attention initiated.'
        }
        return Response(data)

    @action(detail = True, methods = ['get'])
    def finish_attention(self, request, pk = None):
        ticket = self.get_object()
        ticket.finish_time = datetime.now()
        init = timedelta(
            hours = ticket.init_time.hour,
            minutes = ticket.init_time.minute,
            seconds = ticket.init_time.second
        )
        finish = timedelta(
            hours = ticket.finish_time.hour,
            minutes = ticket.finish_time.minute,
            seconds = ticket.finish_time.second
        )
        final = finish - init
        ticket.attention_time = (datetime.min + final).time()
        ticket.status = 'ATT'
        ticket.save()
        data = {
            'message': 'Time attention finished.'
        }
        return Response(data)

    @action(detail = True, methods = ['get'])
    def defer(self, request, pk = None):
        ticket = self.get_object()
        if ticket.deferred:
            ticket.status = 'DFR'
        else:
            ticket.status = 'NAT'
        ticket.deferred = True
        ticket.save()
        data = {
            'message': 'Ticket deferred.'
        }
        return Response(data)
