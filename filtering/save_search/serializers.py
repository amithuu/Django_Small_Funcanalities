from save_search.models import Cricketer, Saved_Search
from rest_framework import serializers

class Cricketer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cricketer
        fields = '__all__'
      
      
class Saved_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Saved_Search
        fields = '__all__'
        
