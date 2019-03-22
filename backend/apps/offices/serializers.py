# Django Rest Framework
from rest_framework import serializers

# Models
from apps.offices.models import Office, Domain


class OfficeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'

    def create(self, validated_data):
        office = Office(
            schema_name = validated_data['schema_name'],
            code = validated_data['code'],
            name = validated_data['name']
        )
        office.save()
        domain = Domain(
            domain = validated_data['schema_name'],
            tenant_id = office.code,
        )
        domain.save()
        return office
