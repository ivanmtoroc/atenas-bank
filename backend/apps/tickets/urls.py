# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Viewsets
from apps.tickets.viewsets import TicketViewSet

app_name = 'tickets'

router = routers.DefaultRouter()
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
