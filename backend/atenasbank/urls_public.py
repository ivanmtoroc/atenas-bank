# Django
from django.conf.urls.static import static
from django.conf import settings

# Rest Framework
from rest_framework import routers

# Apps viewsets
from apps.ads.viewsets import AdViewSet
from apps.clients.viewsets import ClientViewSet
from apps.offices.viewsets import OfficeViewSet
from apps.users.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'ads', AdViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'offices', OfficeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
