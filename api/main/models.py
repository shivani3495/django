from django.db import models
#from rest_framework.fields import ChoiceField

# Create your models here.
class Women(models.Model):
 name = models.CharField(max_length=50)
 age = models.IntegerField()
 dress = models.CharField(max_length=50)
 color = models.CharField(max_length=50)
 passby = models.CharField(max_length=50)  