# Django
from django.db import models

class Client(models.Model):
    identification = models.CharField(max_length = 10, unique = True, primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    is_vip = models.BooleanField(default = False)
    is_active= models.BooleanField(default = True)

    def __str__(self):
        return self.first_name + self.last_name

    REQUIRED_FIELDS = ['identification', 'first_name', 'last_name', 'email', 'phone','address']

