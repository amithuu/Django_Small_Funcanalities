
from rest_framework import serializers
from sort.models import Movie#, Saved_Search

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields  = '__all__'
        

# class Saved_Serializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Saved_Search
#         fields = '__all__'
