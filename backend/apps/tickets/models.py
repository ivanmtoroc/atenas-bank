# Django
from django.db import models

ACTIVITIES = (
    ('GEN', 'General'),
    ('IAE', 'Imports and exports'),
    ('INS', 'Insurances'),
    ('DOT', 'Dollar transactions'),
    ('VIP', 'VIP client')
)

STATUS = (
    ('ATT', 'Attended'),
    ('NAT', 'No Attended'),
    ('DEF', 'Deferred')
)

class Ticket(models.Model):   
    turn_number = models.CharField(max_length = 3)
    user = models.CharField(max_length = 20)
    is_user_vip = models.BooleanField(default = False)
    activity = models.CharField(max_length = 20, choices = ACTIVITIES)
    status = models.CharField(max_length = 20, choices = STATUS)
    is_active = models.BooleanField(default = True)
    time_arrive = models.TimeField(auto_now_add=True)
    init_time = models.TimeField()
    finish_time = models.TimeField()
    total_time = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)





    def __str__(self):
        return self.name
        
