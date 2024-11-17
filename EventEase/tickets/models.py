from django.db import models
from events.models import Event
from django.utils.timezone import now


# Create your models here.
class Ticket(models.Model):
    
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False)
    quantity_available = models.PositiveIntegerField(null=True, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    created_at = models.DateTimeField(default=now)


    def __str__(self):
        return f"{self.ticket_type} - {self.event.title}"
