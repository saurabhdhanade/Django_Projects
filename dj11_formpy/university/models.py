from django.db import models

# Create your models here.

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(max_length=8)
    def __str__(self):
        return self.name