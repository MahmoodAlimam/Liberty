from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Client

# Create the form.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #dob = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    #def save(self, commit=True):
    #    user = super(NewUserForm, self).save(commit=False)
    #    user.email = self.cleaned_data['email']
    #    #user.dob = self.cleaned_data['dob']
    #    if commit:
    #        user.save()
    #    return user

