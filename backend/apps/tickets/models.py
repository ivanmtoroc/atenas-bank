# Django
from django.db import models

ACTIVITIES = (
    ('GEN', 'General'),
    ('IAE', 'Imports and exports'),
    ('INS', 'Insurances'),
    ('DOT', 'Dollar transactions'),
    ('VIP', 'VIP client')
)

class Ticket(models.Model):   
    turn_number = models.CharField(max_length = 3)
    user = models.CharField(max_length = 20)
    user_vip = models.CharField(max_length = 20)
    activity = models.CharField(max_length = 20, choices = ACTIVITIES)
    status = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
        
