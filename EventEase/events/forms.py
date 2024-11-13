
from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',    # HTML5 date input for calendar picker
                'class': 'form-control',
                'placeholder': 'Select Date'
            }
        )
    )
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'type': 'time',    # HTML5 time input for time picker
                'class': 'form-control',
                'placeholder': 'Select Time'
            }))
    class Meta:
        model = Event
        fields = ['title', 'description','image', 'date','ticket_price', 'time', 'location', 'capacity']