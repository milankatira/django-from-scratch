from django.urls import path
from form_api import views

urlpatterns = [
    path('registration/', views.showformdata),
]