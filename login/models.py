from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Register(models.Model):
    user_id=models.IntegerField()
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    Email=models.EmailField()
    Phno=models.CharField(max_length=15)
    pwd=models.CharField(max_length=15)
    cpwd=models.CharField(max_length=15)

class Item(models.Model):
    item_id=models.IntegerField
    itemname=models.CharField(max_length=255)
    itemimages=models.CharField(max_length=255)
    Itemcategory=models.CharField(max_length=50)
    Itemdescription=models.CharField(max_length=1500)
    Dateposted=models.DateField()
    Itemprice=models.IntegerField()
    Itemstatus=models.CharField(max_length=50)
    Dateofremoval=models.DateField()



