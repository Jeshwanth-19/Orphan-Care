from django.db import models
import datetime
# Create your models here. 
class Care(models.Model):
    Organizationname = models.CharField(max_length=50)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Dateofbirth=models.DateTimeField()
    Emailfield = models.EmailField(max_length = 50)
    Contactnumber = models.IntegerField()
    Eadhar = models.IntegerField()
    Establish=models.IntegerField()
    Govtissueid = models.CharField(max_length=50)
    Numberoforphans = models.IntegerField()
    Upi=models.IntegerField()
    Accountdetails=models.TextField()
    Address = models.CharField(max_length=50)
    Village = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Pincode = models.IntegerField()
    Description=models.TextField()
    def __str__(self):
        return self.Organizationname


class Details(models.Model):
    organizationname=models.CharField(max_length=50)
    description=models.TextField()
    firstname = models.CharField(max_length=50)
    establishyear = models.IntegerField()
    govtissueid = models.CharField(max_length=50)
    numberoforphans = models.IntegerField()
    accountdetails=models.TextField()
    address = models.CharField(max_length=50)
    village = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    contactnumber = models.IntegerField()
    def __str__(self):
        return self.organizationname

