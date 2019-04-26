# Django
from django.db import models

SERVICES = (
    ('GEN', 'General'),
    ('IAE', 'Imports and exports'),
    ('INS', 'Insurances'),
    ('DOT', 'Dollar transactions'),
    ('VIP', 'VIP client')
)

STATUS = (
    ('ATT', 'Attended'),
    ('IAT', 'In attention'),
    ('NAT', 'No attended'),
    ('OHL', 'On hold'),
    ('DFR', 'Deferred')
)

class TicketModel(models.Model):
    turn_number = models.CharField(max_length = 6, default = '')
    user = models.CharField(max_length = 10)
    service = models.CharField(max_length = 3, choices = SERVICES)
    status = models.CharField(max_length = 3, choices = STATUS, default = 'NAT')
    deferred = models.BooleanField(default = False)
    date = models.DateField(auto_now_add = True)
    time_arrive = models.TimeField(auto_now_add = True)
    init_time = models.TimeField(null = True)
    finish_time = models.TimeField(null = True)
    attention_time = models.TimeField(null = True)

    def __str__(self):
        return self.turn_number

    def set_turn_number(self):
        my_turn = TicketModel.objects.filter(service = self.service).count()
        self.turn_number = self.service + '{0:0=3d}'.format(my_turn)
