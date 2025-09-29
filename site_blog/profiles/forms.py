from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateFrom(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']