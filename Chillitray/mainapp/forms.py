from django import forms
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import DateInput, PasswordInput,TextInput
from django.contrib.auth.models import User
import re

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput,label="Password")
    password2 = forms.CharField(widget=PasswordInput,label="Repeat password")

    class Meta:
        model=User
        fields = ["username","first_name","last_name","email"]
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match.")
        return cd['password2']

    def clean_username2(self):
        reg = r'^[a-zA-Z]{7,15}\d'
        cd = self.cleaned_data
        print(cd['username'])
        if not (re.search(reg,cd["username"])):
            raise forms.ValidationError("Username is not valid.")
        return cd["username"]