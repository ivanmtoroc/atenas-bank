from django.urls import path
from .views import new_user, login_view, logout_view, change_status


app_name = 'users'

urlpatterns = [
    path('', new_user, name='new'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('change_status/', change_status, name='change_status'),
]
