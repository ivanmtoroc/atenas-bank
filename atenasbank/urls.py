from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls', namespace='users')),
]
