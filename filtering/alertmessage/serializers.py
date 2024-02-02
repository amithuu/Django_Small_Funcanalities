from rest_framework import serializers
from alertmessage.models import Job

class JobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = "__all__"
        

