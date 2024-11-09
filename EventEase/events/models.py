from django.db import models
from users.models import Profile

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'organizer'})
    is_active = models.BooleanField(default=True)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

 
    





    

