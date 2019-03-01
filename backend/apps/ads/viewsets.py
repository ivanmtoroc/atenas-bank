# Django Rest Framework
from rest_framework.response import Response
from rest_framework import viewsets

# Serializers
from apps.ads.serializers import AdSerializer

# Models
from apps.ads.models import Ad


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def destroy(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.is_active = not ad.is_active
        ad.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)
