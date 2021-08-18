from django.urls import path
from register import views

urlpatterns = [
    path('std/',views.studentinfo)
]