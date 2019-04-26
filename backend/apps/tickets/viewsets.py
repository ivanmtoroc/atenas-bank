# Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Datetime
from datetime import datetime, date, timedelta

# Tickets models
from apps.tickets.models import TicketModel

# Tickets serializers
from apps.tickets.serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = TicketModel.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        ticket = serializer.save()
        ticket.set_turn_number()
        ticket.save()

    @action(detail = True, methods = ['get'])
    def init_attention(self, request, pk = None):
        ticket = self.get_object()
        ticket.init_time = datetime.now()
        ticket.status = 'IAT'
        ticket.save()
        data = { 'message': 'Time attention initiated.' }
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
        data = { 'message': 'Time attention finished.' }
        return Response(data)

    @action(detail = True, methods = ['get'])
    def defer(self, request, pk = None):
        ticket = self.get_object()
        if ticket.deferred:
            ticket.status = 'DFR'
        else:
            next_ticket = Ticket.objects.filter(date = date.today(), service = ticket.service, status = 'NAT').order_by('time_arrive').first()
            if next_ticket:
                time = timedelta(
                    hours = next_ticket.time_arrive.hour,
                    minutes = next_ticket.time_arrive.minute,
                    seconds = next_ticket.time_arrive.second + 1
                )
                ticket.time_arrive = (datetime.min + time).time()
            ticket.status = 'NAT'
        ticket.deferred = True
        ticket.save()
        data = { 'message': 'Ticket deferred.' }
        return Response(data)
