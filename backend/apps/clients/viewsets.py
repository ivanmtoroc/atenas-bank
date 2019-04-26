# Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Client models
from apps.clients.models import ClientModel

# Client serializers
from apps.clients.serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        client = self.get_object()
        client.is_active = not client.is_active
        client.save()
        data = { 'message': 'Deleted successfully.' }
        return Response(data)
