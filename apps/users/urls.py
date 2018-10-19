from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
