from django.db import models
from users.models import Profile

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null=True)  # Link each event to a user
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    ticket_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True) 
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

 
    





    

