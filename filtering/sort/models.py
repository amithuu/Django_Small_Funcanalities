from django.db import models
# from django.contrib.auth.models import User  
# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=20)
    movie_desc = models.CharField(max_length=150)
    movie_status = models.BooleanField(default=True)
    avr_rating  = models.FloatField(default=0)
    total_ratings = models.IntegerField(default=0)
    movie_created = models.IntegerField()
    
    def __str__(self):
        return self.movie_name
    

# class Saved_Search(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     saved = models.URLField()
    
#     def __str__(self):
#         return self.saved
