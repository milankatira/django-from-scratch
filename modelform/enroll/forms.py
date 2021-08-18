from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
 class Meta:
  model = User
  fields = ['name', 'password', 'email']
  label = {'name':'enter your name'}
  error_messages = {
   'name':{'required':'enter your Name'},
   'password':{'required':'enter your Password '}
  }
  widgets = {
   'password':forms.PasswordInput,
   'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'write here your name'})
  }
