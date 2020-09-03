from django.db import models
import datetime
# Create your models here.


class Members(models.Model):
    name=models.CharField(max_length=100,)
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField(null=True,blank=True)
    designation=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(max_length=8,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    blood=models.CharField(max_length=100,null=True,blank=True)



    def __str__(self):
        return self.name
