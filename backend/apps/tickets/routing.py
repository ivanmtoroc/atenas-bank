# Django
from django.conf.urls import url

# Consumers
from .consumers import TicketsConsumer

websocket_urlpatterns = [
    url('ws/tickets/', TicketsConsumer),
]
