from django import forms
from .models import CustomUserModel
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + (
            'first_name', 'last_name', 'email', 'bio', 'image', 'instagram', 'telegram', 'site',
        )  # type: ignore


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUserModel
        fields = UserChangeForm.Meta.fields

