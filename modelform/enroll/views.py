from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def showformdata(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   reg=User(name='nm',email='em',password='pw')
   reg.save() #for save in database
   #print(nm)
   #print(em)
   #akemigrations
   # print(pw)
 else:
  fm = StudentRegistration()

 return render(request, 'enroll/userregistration.html', {'form':fm})
