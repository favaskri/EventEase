from django.db import models
from events.models import Event
from users.models import User

# Create your models here.

class VenueRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    company_organization = models.CharField(max_length=100)
    venue_requested = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    from_datetime = models.DateTimeField()  # Start date and time
    to_datetime = models.DateTimeField()    # End date and time
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    about_event_hosting = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.venue_requested}"

# # Create your models here.

# class Registration(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=20)
#     company_organization = models.CharField(max_length=100)
#     password= models.TextField()
    

#     def __str__(self):
#         return f"{self.user.username} - {self.venue_requested}"

    
 