from django import forms
from django.core import validators

class StudentRegistration(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput,label='Password(again)')

#password match and validation
def clean(self):
    cleaned_data = super().clean()
    mypassword=self.cleaned_data['password']
    checkpassword=self.cleaned_data['confirm_password']
    print(mypassword)
    print(checkpassword)
    if mypassword!=checkpassword:
        raise forms.ValidationError('password does not match')