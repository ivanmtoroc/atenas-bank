# Django
from django.db import models

# Django Tenants
from django_tenants.models import TenantMixin, DomainMixin


class Office(TenantMixin):
    code = models.CharField(max_length = 3, primary_key = True)
    name = models.CharField(max_length = 20)
    employees = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    pass
