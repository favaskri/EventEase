from django.contrib import admin
from .models import Registration  # Import the registration model

# Register the registration model with the admin site
admin.site.register(Registration)