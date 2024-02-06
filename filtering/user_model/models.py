from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager
# Create your models here.

class CustomerUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.IntegerField(unique=True)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
