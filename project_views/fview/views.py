from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#function based views
def my_func(request):
    return HttpResponse('<h1>hello django</h1>')
