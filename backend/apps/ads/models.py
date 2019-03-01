# Django
from django.db import models

class Ad(models.Model):   
    description = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'ads/')
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.description
