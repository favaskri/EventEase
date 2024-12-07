from django.db import models
from events.models import Event
from users.models import User
from django.utils.timezone import now
# from uuid import uuid4



# Create your models here.
class Ticket(models.Model):
    
    ticket_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=False,default=0.00)
    quantity_available = models.PositiveIntegerField(null=True, blank=True)
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    created_at = models.DateTimeField(default=now)
    # ticket_id = models.UUIDField(default=uuid4, editable=False, unique=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    ticket_remaining=models.IntegerField(null=True,blank=True)

    def save(self ,*args,**kwargs):
        self.price = self.event.ticket_price
        self.total_price = self.price * self.quantity

        if self.event.available_tickets<=0:
            raise ValueError("No tickets available for this event!")
        # self.event.available_tickets-=1
        # self.event.save()

        self.ticket_remaining=self.event.available_tickets

        # Now call the parent class's save method to save the ticket instance itself
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_type} - {self.event.title}"


    


    def __str__(self):
        return f"{self.ticket_type} - {self.event.title}"
