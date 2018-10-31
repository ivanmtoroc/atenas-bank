from django.db import models


ACTIVITIES = (
    ('CRP', 'Consignaciones, retiros y pagos de servicios'),
    ('IE', 'Importaciones y exportaciones'),
    ('S', 'Seguros'),
    ('TD', 'Transacciones en dolares'),
    ('VIP', 'Clientes VIP')
)

class TicketRequestForm(models.Model):
    activity = models.CharField(max_length = 20, choices = ACTIVITIES)
    cedula = models.CharField(max_length = 10)
