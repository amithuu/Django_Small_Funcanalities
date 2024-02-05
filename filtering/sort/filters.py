
import django_filters
from sort.models import Movie

class MovieFilter(django_filters.FilterSet):
    total_ratings = django_filters.RangeFilter()
    
    class Meta:
        model = Movie
        fields = {
            'movie_name':['icontains'],
            'movie_desc':['icontains'],
            'movie_status':['exact'],
            'avr_rating':['lt', 'gt'],
            'movie_created':['icontains']
        }