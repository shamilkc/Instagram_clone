from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


class UserCreationForm(ModelForm):
    bio = forms.CharField(max_length=250)
    image = forms.ImageField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password", "bio", "image"]


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", ]
