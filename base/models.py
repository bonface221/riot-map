from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='mapImages', blank=True)
    description = models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f'{self.name} Location'

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.user} Account'

    
