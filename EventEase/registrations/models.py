from django.db import models
from events.models import Event
from users.models import Profile

# Create your models here.
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'attendee'})
    registration_date = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.attendee.user.username} - {self.event.title}"
