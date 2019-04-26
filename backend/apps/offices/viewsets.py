# Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Offices models
from apps.offices.models import OfficeModel, DomainModel

# Offices serializers
from apps.offices.serializers import OfficeSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = OfficeModel.objects.all()
    serializer_class = OfficeSerializer

    def destroy(self, request, *args, **kwargs):
        office = self.get_object()
        office.is_active = not office.is_active
        office.save()
        data = { 'message': 'Deleted successfully.' }
        return Response(data)

    def perform_update(self, serializer):
        office = serializer.save()
        domain = DomainModel.objects.get(tenant_id = office.id)
        domain.domain = office.schema_name + '.localhost'
        domain.save()
