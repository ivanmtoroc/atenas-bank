# Django
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', include('apps.users.urls', namespace = 'users')),
    path('', include('apps.offices.urls', namespace = 'offices')),
    path('', include('apps.ads.urls', namespace = 'ads')),
    path('', include('apps.clients.urls', namespace = 'clients')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
