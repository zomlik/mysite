from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField(primary_key='id',unique='id')
    login = models.CharField(max_length=16)
    passward = models.CharField(max_length=16)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    sex = models.CharField(max_length=1)
    city = models.CharField(max_length=64)
