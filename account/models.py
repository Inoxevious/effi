from django.db import models
from django.contrib.auth.models import User


class UserClass(models.Model): 
    name = models.CharField(max_length=70)
    user_group = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=70)
    user_group = models.CharField(null=True ,blank=True,max_length=255)

    def __str__(self):
        return self.name

class Country(models.Model): 
    name = models.CharField(max_length=200, default='zim')
    official_language = models.TextField(null=True ,blank=True)
    flag = models.ImageField(null=True ,blank=True, upload_to='static/images/countries/flags')
    longi = models.TextField(null=True ,blank=True)
    lat = models.TextField(null=True ,blank=True) 

# Create your models here.
class AccountUser(models.Model):
    role = models.CharField(null=True ,blank=True,max_length=70)
    category = models.CharField(null=True ,blank=True,max_length=70)
    age = models.IntegerField(null=True ,blank=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # country =  models.ForeignKey(Country, on_delete=modelon_delete=models.CASCADEs.CASCADE, default=0)
    email_confirmed = models.BooleanField(default=False)
    address =models.TextField(null=True ,blank=True)
    date_birth =models.DateField(null=True ,blank=True)
    phone =models.CharField(null=True ,blank=True,max_length=70)
    id_number =models.CharField(null=True ,blank=True,max_length=20)
    gender =models.CharField(null=True ,blank=True,max_length=20)
    education_level =models.CharField(null=True ,blank=True,max_length=70)
    marital_status =models.CharField(null=True ,blank=True,max_length=20)
    number_dependants =models.IntegerField(null=True ,blank=True)
    total_worth =models.IntegerField(null=True ,blank=True)
    profile_pic = models.ImageField(null=True ,blank=True, upload_to='staticfiles/images')
    

    def __str__(self):
        return self.user.username
