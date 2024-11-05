from django.contrib import admin
from .models import Event  # Import the Event model

# Register the Event model with the admin site
admin.site.register(Event)