# Django Rest Framework
from rest_framework.response import Response
from rest_framework import viewsets

# Serializers
from apps.offices.serializers import OfficeSerializer

# Models
from apps.offices.models import Office

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

    def destroy(self, request, *args, **kwargs):
        office = self.get_object()
        office.is_active = not office.is_active
        office.save()
        data = {
            'message': 'Delete success.'
        }
        return Response(data = data)
