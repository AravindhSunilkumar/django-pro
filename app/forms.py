# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# forms.py
from django import forms

from .models import add_profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = add_profile
        fields = ['name', 'phone_number', 'profileimg']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = add_profile
        fields = ['name', 'phone_number', 'profileimg']
