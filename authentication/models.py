from math import degrees
from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField(max_length=70)
    college_name=models.CharField(max_length=70)
    Specialisation=models.CharField(max_length=70)
    degree=models.CharField(max_length=70)
    internship=models.CharField(max_length=70)
    phoneNo=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    location=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    notes=models.CharField(max_length=200)




