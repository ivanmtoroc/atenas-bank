# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Viewsets
from apps.offices.viewsets import OfficeViewSet


app_name = 'offices'

router = routers.DefaultRouter()
router.register(r'offices', OfficeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
