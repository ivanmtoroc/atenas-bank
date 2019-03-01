# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Viewsets
from backend.apps.ads.viewsets import AdViewSet

app_name = 'ads'

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
