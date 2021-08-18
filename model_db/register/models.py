from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    Student_name=models.CharField(max_length=100)
    Student_mail=models.EmailField(max_length=100)
    Student_pass=models.CharField(max_length=100)
'''
here we have to define class of our database table with we want to create 

then register class to admin.py file for access by admin panel
'''



def __str__(self):
    return self.student_id

'''
here def __str__(self):
is used to writen student_name in table name 
'''