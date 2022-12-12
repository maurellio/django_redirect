from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Links

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        User.username = None
        fields = ['username', 'password1', 'password2']

class CreateLink(forms.ModelForm):
    class Meta:
        model = Links
        fields = ['name', 'url_link']