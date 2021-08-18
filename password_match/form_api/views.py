from django.shortcuts import render
from .form import StudentRegistration

# Create your views here.
def showformdata(request):
    if request.method=='POST':
       fm=StudentRegistration(request.POST)
       if fm.is_valid():
           print('form valideted')
           print('Name',fm.cleaned_data['name'])
           print('Email',fm.cleaned_data['email'])
           print('password',fm.cleaned_data['password'])
           print('confirm_password',fm.cleaned_data['confirm_password'])
    else:
        fm = StudentRegistration (request.POST)
        print("output is from get request ")

    #fm=StudentRegistration(auto_id=True, label_suffix=' ', initial={ 'name':'milan'})
    #fm.order_fields(field_order=['email','name','first_name']) #field order preferance 
    return render (request, 'enroll/user.html', {'form':fm })