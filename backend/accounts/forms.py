from django import forms
from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }