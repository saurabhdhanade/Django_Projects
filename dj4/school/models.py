from django.db import models

# Create your models here.

class Exam(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    center=models.CharField(max_length=100)
    rollnum=models.BigIntegerField()
    examdate=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phn=models.IntegerField()
    add=models.TextField()
    
    def __str__(self):
        return self.name
