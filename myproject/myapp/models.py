from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class empl(models.Model):
    first_name=models.CharField(verbose_name="first Name",max_length=30)
    Last_name=models.CharField(verbose_name="Last Name",max_length=5)
    Email=models.CharField(verbose_name="Email ID",max_length=30)
    Mobile_num=models.IntegerField(verbose_name="mobile Number",max_length=12)
    # class Meta:
    #     db_table="Employe Data"

class Emplo(models.Model):
    First_Name=models.CharField(verbose_name="FIRST NAME",max_length=15)
    Last_Name=models.CharField(verbose_name="LAST NAME",max_length=5)
    Gmail=models.CharField(verbose_name="GMAIL",max_length=20)
    mobile=models.IntegerField(verbose_name='mobile number')
    password=models.CharField(verbose_name='password',max_length=8)
    class meta:
        db_table="EMPLOYE DATA"
        
class Tech(models.Model):
    fname=models.CharField(max_length=14)
    photo=models.ImageField(upload_to='uploded_images/')


#crud

class crud(models.Model):
    NAME=models.CharField(max_length=15)
    LAST_NAME=models.CharField(max_length=5)
    AGE=models.IntegerField(max_length=2)
    GMAIL=models.CharField(max_length=10)
    class Meta:
        db_table="CRUD OPERATIONS"

class