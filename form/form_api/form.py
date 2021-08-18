from django import forms
from django.core import validators
def starts_with_m(value):
    if value[0] !='m':
        raise forms.ValidationError('name should start with m')

class StudentRegistration(forms.Form):
    #myname=forms.CharField(min_length=5,max_length=10,strip=False )
    #lname=forms.CharField(validators=[starts_with_m])
    name = forms.CharField(error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'})
    #name=forms.CharField(min_length=5,max_length=10,empty_value='milan')
    #email=forms.EmailField(label='email-id',label_suffix=' ',initial='example@gmail.com',
    #required=True,disabled=False, help_text='limit 50 characters')
    #roll=forms.IntegerField(max_value=5)
    #agree=forms.BooleanField( label_suffix='',label='i agree')
    #price=forms.DecimalField( min_value=5,max_value=45,decimal_places=1)
    #first_name=forms.CharField(widget=forms.PasswordInput) #here in fiart_name _is used as scape in output 
    #box=forms.CharField(widget=forms.CheckboxInput)
    #fileinput=forms.CharField(widget=forms.FileInput)
    def clean_name(self):
        mname=self.cleaned_data['name']
        if len(mname)< 7:
            raise forms.ValidationError('enter more than 7')
        return mname
