# Django
from django.urls import path

# Tickets consumers
from apps.tickets.consumers import TicketsConsumer

websocket_urlpatterns = [
    path('<str:tenant>', TicketsConsumer),
]
