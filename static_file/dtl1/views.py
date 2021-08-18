from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request,'dtl1/course.html')
