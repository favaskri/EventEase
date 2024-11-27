
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from .models import Profile
# """from .models import Profile"""  

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
#     phone_number = forms.CharField(max_length=15, required=True, help_text="Required. Enter a valid phone number.")
#     role=forms.ChoiceField(
#                 choices=Profile.ROLE_CHOICES,
#                 widget=forms.RadioSelect,
#                 required=True,
#                 help_text='Select the role for this user'
#                         )
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'phone_number','role']
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")
    phone_number = forms.CharField(max_length=15, required=True, help_text="Required. Enter a valid phone number.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create a Profile with role set to "user" by default
            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number'],
                role='user'  # Default role is "user"
            )
        return user
