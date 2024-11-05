from django.contrib import admin
from .models import Notification # Import the notification model

# Register  model with the admin site
admin.site.register(Notification)