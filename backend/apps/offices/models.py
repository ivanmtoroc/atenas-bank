# Django
from django.db import models

# Tenants
from django_tenants.models import TenantMixin, DomainMixin

class OfficeModel(TenantMixin):
    name = models.CharField(max_length = 20)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class DomainModel(DomainMixin):
    pass
