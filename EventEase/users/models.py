from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Profile(models.Model):
    USER_TYPES = (
        ('organizer', 'Organizer'),
        ('attendee', 'Attendee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    # Additional profile fields (optional)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"
