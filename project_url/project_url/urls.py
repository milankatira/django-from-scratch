"""project_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

'''
#method 1 
from url_1 import views as u1
from url_2 import views as u2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_func1/',u1.my_func_1),
    path('my_func2/',u2.my_func_2),
]
'''

'''
#method 2 
from url_1 import views 
from url_2 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_func1/',views.url_1.my_func_1),
    path('my_func2/',views.url_2.my_func_2),
]
'''

#method 3
from url_1.views import my_func_1
from url_2.views import my_func_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_func1/',my_func_1),
    path('my_func2/',my_func_2),
]
