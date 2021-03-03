from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email','first_name','last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name')