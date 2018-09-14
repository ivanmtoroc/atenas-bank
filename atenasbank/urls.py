from django.contrib import admin
from django.urls import path

# View
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test, name = 'test'),
]
