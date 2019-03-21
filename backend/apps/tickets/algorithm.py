# Django
from .models import Ticket

# Python
from datetime import date, datetime

def next_ticket(service):
    today = date.today()
    ticket = Ticket.objects.filter(date = today, service = service, status = 'NAT').order_by('time_arrive').first()
    if not ticket:
        ticket = Ticket.objects.filter(date = today, service = 'VIP', status = 'NAT').order_by('time_arrive').first()
        if not ticket:
            ticket = Ticket.objects.filter(date = today, status = 'NAT').order_by('time_arrive').first()
            if not ticket:
                return None    
    ticket.status = 'OHL'
    ticket.save()
    return ticket

def init_attention(id):
    ticket = Ticket.objects.get(id = id)
    ticket.init_time = datetime.now()
    ticket.save()
