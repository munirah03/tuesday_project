from django.db import models

# Create your models here.

class Members(models.Model):
    Name = models.TextField(max_length=200)          
    Age = models.IntegerField(default=100)
