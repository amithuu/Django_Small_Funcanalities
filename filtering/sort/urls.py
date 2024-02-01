
from django.urls import path
from sort import views


urlpatterns = [
    path('create', views.MovieCreateView.as_view(), name = 'movie_filter'),
    path('filter', views.MovieListAPIView.as_view(), name = 'movie_filter'),
    
]

