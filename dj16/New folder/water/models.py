from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length = 100)
#     email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length = 100, null = True, blank = True)
    designation = models.CharField(max_length = 100, null = True, blank = True)
    adhar = models.CharField(max_length = 100, null = True, blank = True)
    
    def __str__(self):
        return self.name
