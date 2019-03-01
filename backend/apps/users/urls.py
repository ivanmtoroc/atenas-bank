# Django
from django.urls import path, include

# Django Rest Framework
from rest_framework import routers

# Viewsets
from  backend.apps.users.viewsets import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
