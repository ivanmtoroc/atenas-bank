from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.users.urls', namespace='users')),
    path('home/', include('apps.home.urls', namespace='home')),
    path('tickets/', include('apps.tickets.urls', namespace='tickets')),
]
