# Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Ads models
from apps.ads.models import AdModel

# Ads serializers
from apps.ads.serializers import AdSerializer

class AdViewSet(viewsets.ModelViewSet):
    queryset = AdModel.objects.all()
    serializer_class = AdSerializer

    def destroy(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.is_active = not ad.is_active
        ad.save()
        data = { 'message': 'Deleted successfully.' }
        return Response(data)
