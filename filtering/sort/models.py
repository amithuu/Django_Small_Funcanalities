from django.db import models
 
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
