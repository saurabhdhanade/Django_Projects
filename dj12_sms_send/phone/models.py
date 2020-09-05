from django.db import models
import phone

# Create your models here.
class SendSMS(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    def __str__(self):
        return self.name

