from django.db import models


ACTIVITIES = (
    ('CRP', 'Consignaciones, retiros y pagos de servicios'),
    ('IE', 'Importaciones y exportaciones'),
    ('S', 'Seguros'),
    ('TD', 'Transacciones en dolares'),
    ('VIP', 'Clientes VIP')
)

class Ticket(models.Model):
    number = models.AutoField(primary_key = True)
    cedula = models.CharField(max_length = 10)
    vip = models.BooleanField(default = False)
    activity = models.CharField(max_length = 20, choices = ACTIVITIES, default = 'CRP')
    state = models.BooleanField(default = False)
    date = models.DateField(auto_now_add = True)
    start = models.DateField(null = True)
    end = models.DateField(null = True)

    def __str__(self):
        return '%s%s' % (self.activity, self.number)
