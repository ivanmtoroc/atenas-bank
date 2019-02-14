# Django
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('apps.users.urls', namespace = 'users')),
    path('', include('apps.offices.urls', namespace = 'offices')),
]
