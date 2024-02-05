from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cricketer(models.Model):
    name = models.CharField(max_length=10)
    role = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Saved_Search(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    saved = models.URLField()
    
    def __str__(self):
        return self.saved