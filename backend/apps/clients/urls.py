# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Viewsets
from apps.clients.viewsets import ClientViewSet


app_name = 'clients'

router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
