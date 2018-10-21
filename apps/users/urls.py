from django.urls import path
from .views import users, login_view, logout_view, delete


app_name = 'users'

urlpatterns = [
    path('', users, name = 'crud'),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
    path('delete/', delete, name = 'delete'),
]
