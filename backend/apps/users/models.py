# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

POSITIONS = (
    ('OP', 'Operator'),
    ('MG', 'Manager')
)

class User(AbstractUser):
    identification = models.CharField(max_length = 10, unique = True, primary_key = True)
    username = models.CharField(max_length = 20, unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    position = models.CharField(max_length = 10, choices = POSITIONS)

    def __str__(self):
        return self.username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['identification', 'first_name', 'last_name', 'email', 'position']
