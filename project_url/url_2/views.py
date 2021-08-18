from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_func_2(request):
    return HttpResponse("this is my func 2")