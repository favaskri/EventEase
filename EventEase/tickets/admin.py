from django.contrib import admin
from .models import Ticket  # Import the ticket model

# Register the ticket model with the admin site
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('event','price', 'quantity', 'created_at', 'user')


