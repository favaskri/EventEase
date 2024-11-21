
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
"""from .models import Profile"""  

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    phone_number = forms.CharField(max_length=15, required=True, help_text="Required. Enter a valid phone number.")
    role=forms.ChoiceField(
                choices=Profile.ROLE_CHOICES,
                widget=forms.RadioSelect,
                required=True,
                help_text='Select the role for this user'
                        )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number','role']
