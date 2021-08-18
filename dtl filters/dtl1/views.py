from django.shortcuts import render
from datetime import datetime
# Create your views here.
'''
def learn_django(request):
    return render(request,'dtl1/course.html',{'nm':'django is awosome'})

def learn_django(request):
    return render(request,'dtl1/course.html',{'name':'MILAN'})
'''
def learn_django(request):
    d=datetime.now()
    return render(request,'dtl1/course.html',{'dt':d})
    