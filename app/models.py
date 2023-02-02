from django.db import models

# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=8, unique=True)
    passward = models.CharField(max_length=16)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25, blank=True)
    email = models.CharField(max_length=64, unique=True)
    adress = models.CharField(max_length=64)
    sex = models.CharField(max_length=1)
    city = models.CharField(max_length=64)
    permission = models.CharField(max_length=1)

class Product(models.Model):
    img = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    gender = models.CharField(max_length=1)
    Category_id = models.IntegerChoices()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    


