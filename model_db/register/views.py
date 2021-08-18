from django.shortcuts import render
from register.models import Student
# Create your views here.

def studentinfo(request):
    stud = Student.objects.all()
    print('myoutput',stud)
    return render (request,'studentdetail.html',{'stu':stud})

