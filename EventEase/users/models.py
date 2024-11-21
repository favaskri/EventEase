# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ADMIN='Admin'
    USER='User'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (USER, 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,default=0)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default=USER)

    def __str__(self):
        return self.user.username
