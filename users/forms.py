from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#Local Imports
from .models import CustomUser

#Forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'email', 'username', 'avatar')
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',)
