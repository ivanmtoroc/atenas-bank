# Django
from django.db import models


class Office(models.Model):
    code = models.CharField(max_length = 3, primary_key = True)
    name = models.CharField(max_length = 20)
    employees = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
