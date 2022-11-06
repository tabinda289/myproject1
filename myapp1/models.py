from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    

# class for 3 div portionwith html
#class Feature:
# id: int
   # name: str
    #details: str
    