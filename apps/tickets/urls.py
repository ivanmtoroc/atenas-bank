from django.urls import path
from .views import dashboard, requests


app_name = 'tickets'

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('requests', requests, name = 'requests'),
]
