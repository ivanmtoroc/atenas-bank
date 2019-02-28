# Django Rest Framework
from rest_framework.response import Response
from rest_framework import viewsets

# Serializers
from apps.clients.serializers import ClientSerializer

# Models
from apps.clients.models import Client

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.is_active = not client.is_active
        client.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)
