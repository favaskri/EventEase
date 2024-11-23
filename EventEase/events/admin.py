from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'capacity', 'available_tickets', 'date', 'time')  # Correct field name
