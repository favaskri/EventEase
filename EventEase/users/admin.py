from django.contrib import admin
from .models import Profile  # Import the User model

# Register the user model with the admin site
admin.site.register(Profile)