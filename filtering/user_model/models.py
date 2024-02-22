from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.


auth_providers = {'google':'google', 'email':'email'}

class CustomerUser(AbstractUser):
    
    email = models.EmailField(_('email address'),unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.IntegerField(unique=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
