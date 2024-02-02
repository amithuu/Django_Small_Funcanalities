from django.db import models

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)
    opening_slots = models.IntegerField()
    location = models.CharField(max_length=30)
    include_freshers = models.BooleanField(default=False)
    
    def __str__(self):
        return self.job_title