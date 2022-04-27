from math import degrees
from django.db import models

# Create your models here.
class Plate(models.Model):
    idplate=models.CharField(max_length=70)
    plateNo=models.CharField(max_length=70)
    phoneNo=models.CharField(max_length=100)




