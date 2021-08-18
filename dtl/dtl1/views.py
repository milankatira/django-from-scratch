from django.shortcuts import render

# Create your views here.
def learn_django(request):
    cname='django'
    duration='4 month'
    seats='10'
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'dtl1/course.html',django_details)
