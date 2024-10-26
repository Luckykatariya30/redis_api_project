from django.db import models

# Create your models here.

class Register(models.Model):
    s_name = models.CharField(max_length=121)
    s_roll = models.IntegerField(unique=True)
    s_address = models.CharField(max_length=212)
    city = models.CharField(max_length=121)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=8)
    

