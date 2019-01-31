from django.urls import path, include
from rest_framework import routers
from .viewsets import UserViewSet
from .views import login_view, logout_view
from django.views.generic import TemplateView


app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'users/users.html'), name = 'users'),
    path('api/', include(router.urls)),
    path('login/', login_view, name = 'login'),
    path('logout/', logout_view, name = 'logout'),
]
