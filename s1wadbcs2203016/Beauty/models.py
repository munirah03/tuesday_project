from django.db import models

# Create your models here.

class Customer(models.Model):
    CustName = models.TextField(max_length=200)          
    CustPhone = models.CharField(max_length=100)    
    
class Package(models.Model):
    PackID = models.CharField(max_length=100) 
    PackName = models.TextField(max_length=200)
    PackPrice = models.IntegerField(default=100)
    
class Customer_booking(models.Model):
    BookingNo = models.CharField(max_length=100)
    CustID = models.IntegerField
    PackID = models.CharField(max_length=100) 
    StartDate = models.DateField(null=True)