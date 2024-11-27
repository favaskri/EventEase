# admin_forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AdminLoginForm(AuthenticationForm):
    # You can customize labels or widgets if needed
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    phone_number = forms.CharField(max_length=15, required=True, help_text="Required. Enter a valid phone number.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True  # Mark as staff
        if commit:
            user.save()
            # Create a Profile with role set to "admin" by default
            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                role='admin'  # Default role is "admin"
            )
        return user
