from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    POSITIONS = (
        ('Operator', 'Operator'),
        ('Manager', 'Manager'),
    )
    username = models.CharField(max_length = 20, unique = True)
    cedula = models.CharField(max_length = 10, unique = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 200, unique = True)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)
    position = models.CharField(max_length = 20, choices = POSITIONS)

    def __str__(self):
        return self.username

    @staticmethod
    def list():
        try:
            return User.objects.all()
        except User.DoesNotExist:
            return None

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'cedula', 'position']
    USERNAME_FIELD = 'username'
