# Rest Framework
from rest_framework import serializers

# Offices models
from apps.offices.models import OfficeModel, DomainModel

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'

    def create(self, validated_data):
        office = OfficeModel(
            schema_name = validated_data['schema_name'],
            name = validated_data['name']
        )
        office.save()
        domain = DomainModel(
            domain = validated_data['schema_name'] + '.localhost',
            tenant_id = office.id,
        )
        domain.save()
        return office
