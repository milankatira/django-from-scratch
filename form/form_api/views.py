from django.shortcuts import render
from .form import StudentRegistration
from .models import User
# Create your views here.
def showformdata(request):
    if request.method=='POST':
       fm=StudentRegistration(request.POST)
       if fm.is_valid():
           
           '''
           print('form valideted')
           print('Name',fm.cleaned_data['name'])
           print('Email',fm.cleaned_data['email'])
           #print('price',fm.cleaned_data['price'])
           '''
           
           nm = fm.cleaned_data['name']
           em = fm.cleaned_data['email']
           pw = fm.cleaned_data['password']
           print(nm)
           print(em)
           print(pw)

           '''
           reg = User(name=nm, email=em, password=pw)
           reg = User(id=1, name=nm, email=em, password=pw)
           #reg.save()
           #reg = User(id=1)
           #reg.delete()
           '''
       else:
           fm = StudentRegistration()

    return render(request,'enroll/user.html',{'form':fm})


    #fm=StudentRegistration(auto_id=True, label_suffix=' ', initial={ 'name':'milan'})
    #fm.order_fields(field_order=['email','name','first_name']) #field order preferance 
    



