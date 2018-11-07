from django.contrib.auth.models import AbstractUser
from django.db import models


POSITIONS = (
    ('OPT', 'Operator'),
    ('MNG', 'Manager')
)

class User(AbstractUser):
    cedula = models.CharField(max_length = 10, unique = True, primary_key = True)
    username = models.CharField(max_length = 20, unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    position = models.CharField(max_length = 20, choices = POSITIONS)

    def __str__(self):
        return self.username

    REQUIRED_FIELDS = ['cedula', 'first_name', 'last_name', 'email', 'position']
    USERNAME_FIELD = 'username'
