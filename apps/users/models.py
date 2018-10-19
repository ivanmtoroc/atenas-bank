from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    created = models.DateField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username

    @staticmethod
    def list():
        try:
            return Profile.objects.all()
        except Profile.DoesNotExist:
            return None
