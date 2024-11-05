from django.db import models
from events.models import Event

# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    amenities = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class EventVenue(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    booking_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.venue.name} - {self.event.title}"
