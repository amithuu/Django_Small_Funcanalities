from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from alertmessage.serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.validators import ValidationError
# Create your views here
from alertmessage.utils import Send_Notification


        
class JobCreateAPIView(CreateAPIView):
    serializer_class = JobSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data = request.data)
            
            if not serializer.is_valid(raise_exception=False):
                return Response({'message':'Not able to create job', 'error': ValidationError(serializer.errors)})
            else:
                serializer.save()
                
                Send_Notification().send_email(
                    body='congratulations on Creating the job..',
                    subject='Posted a Job',
                    to='amithkulkarni99@gmail.com'
                    )
                                
                return Response({'message':'successfully created job','data':serializer.data})
        
        except Exception as e:
            return Response({'message':'failed to create job','error':str(e)})    
        
        
            
