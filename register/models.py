from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length= 50, unique=True)
    username = models.CharField(max_length= 50, unique=True)
    password = models.CharField(max_length= 256)
    tel = models.IntegerField()
    email = models.EmailField(max_length= 70, unique=True, blank=True)
    address = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.username