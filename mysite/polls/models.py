from django.db import models

# Create your models here.
class Contact(models.Model):
    name =models.CharField(max_length=100)
    email =models.EmailField(max_length=25)
    phone =models.CharField(max_length=15)
    content =models.TextField(max_length=50)