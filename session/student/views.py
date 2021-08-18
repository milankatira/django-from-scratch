from django.shortcuts import render
'''
# Create your views here.
def setsession(request):
 request.session['name'] = 'milan'
 request.session['lname'] = 'katira'
 return render(request, 'student/setsession.html')

def getsession(request):
 # name = request.session['name']
 name = request.session.get('name')
 lname = request.session.get('lname')
 return render(request, 'student/getsession.html', {'name':name, 'lname':lname})

def delsession(request):
 if 'name' in request.session:
  del request.session['name']
 return render(request, 'student/delsession.html')




# Create your views here.
def setsession(request):
 request.session['name'] = 'milan'
 request.session['lname'] = 'katira'
 return render(request, 'student/setsession.html')

def getsession(request):
 name = request.session.get('name')
 keys = request.session.keys()
 items = request.session.items()
 # age = request.session.setdefault('age', '21')
 return render(request, 'student/getsession.html', {'name':name, 'keys':keys, 'items':items})

def delsession(request):
 request.session.flush()
 return render(request, 'student/delsession.html')
'''


def setsession(request):
 request.session['name'] = 'milan'
 request.session.set_expiry(10)
 return render(request, 'student/setsession.html')

def getsession(request):
 name = request.session['name']
 print(request.session.get_session_cookie_age())
 print(request.session.get_expiry_age())
 print(request.session.get_expiry_date())
 print(request.session.get_expire_at_browser_close())
 return render(request, 'student/getsession.html', {'name':name})

def delsession(request):
 request.session.flush()
 request.session.clear_expired()
 return render(request, 'student/delsession.html')

 