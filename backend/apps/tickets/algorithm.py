# Tenants
from django_tenants.utils import schema_context

# Django
from apps.tickets.models import TicketModel

# Datetime
from datetime import date, datetime

def next_ticket(service, tenant):    
    with schema_context(tenant):
        today = date.today()
        ticket = TicketModel.objects.filter(date = today, service = service, status = 'NAT').order_by('time_arrive').first()
        if not ticket:
            ticket = TicketModel.objects.filter(date = today, service = 'VIP', status = 'NAT').order_by('time_arrive').first()
            if not ticket:
                ticket = TicketModel.objects.filter(date = today, status = 'NAT').order_by('time_arrive').first()
                if not ticket:
                    return None
        ticket.status = 'OHL'
        ticket.save()
        return ticket
