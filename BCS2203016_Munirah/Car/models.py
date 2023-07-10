from django.db import models

# Create your models here.

class Client(models.Model):
    ClientId = models.CharField(max_length=100, primary_key=True)          
    ClientName = models.TextField(max_length=100) 
    ClientPhone = models.CharField(max_length=100)
    Gender = models.TextField(max_length=100)
    
class Car(models.Model):
    CarPlate = models.CharField(max_length=100, primary_key=True)
    Type = models.TextField(max_length=100)
    Capacity = models.IntegerField(default=100)
    CarStatus = models.TextField(default='Ok')
    
class Rental_record(models.Model):
    ClientId = models.ForeignKey(Client, on_delete=models.CASCADE) 
    CarPlate = models.ForeignKey(Car, on_delete=models.CASCADE)
    TotalPaid = models.IntegerField(default=100)
    StartDate = models.DateField(null=True)
    ReturnDate = models.DateField(null=True)
    
