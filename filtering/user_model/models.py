from django.db import models
from django.contrib.auth.models import AbstractUser 
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
from filtering import settings 
# Create your models here.

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
    

class OtpLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=200,null=True)
    otp = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=10,null=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email
    
# https://cv-builder.talentplace.ai/uploads
# def avatar(instance,filename):
#     return 'uploads/{}/{}'.format(instance.user_id, filename)

 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatar', blank=True)
    bio = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.user.email