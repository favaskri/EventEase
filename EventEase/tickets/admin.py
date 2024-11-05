from django.contrib import admin
from .models import Ticket  # Import the ticket model

# Register the ticket model with the admin site
admin.site.register(Ticket)