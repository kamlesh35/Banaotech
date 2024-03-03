from django.db import models
from django import forms
# Create your models here.



class Doctor(models.Model):
    username = models.CharField( max_length=50)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    Email =  models.EmailField(max_length=254)
    contact = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.username
   
    def clean(self):
        clean_data = super().clean()
        valpass = self.clean_data('password')
        revalpass = self.clean_data('valpass')
        if valpass!=revalpass:
            raise models.ValidationError("Password is not matching")


class Patient(models.Model):
    username = models.CharField( max_length=50)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    Email =  models.EmailField(max_length=254,unique = True)
    contact = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    
    def __str__(self):
        return self.first_name
    


