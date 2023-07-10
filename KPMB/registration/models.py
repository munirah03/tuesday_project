from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=4, primary_key=True)
    desc = models.TextField(max_length=128)             
  
