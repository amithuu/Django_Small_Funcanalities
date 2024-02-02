from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from alertmessage.serializers import JobSerializer
from alertmessage.models import Job
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
        
        
class JobListAPIView(ListAPIView):
    serializer_class =JobSerializer
    
    def get(self, request, *args, **kwargs):
        try:
            queryset = Job.objects.all()
            
            query_list = {
                'title' : 'job_title__icontains',
                'location':'location__icontains',
                'type': 'job_type__icontains', 
                'include_freshers' : 'include_freshers',
            }
            
            filters = {}
            
            for param, model_name in query_list.items():
                value = self.request.query_params.get(param, None)
                if value:
                    filters[model_name] = value
            queryset = queryset.filter(**filters)
            
            serializer = self.get_serializer(queryset, many=True).data

            if serializer:
                return Response({'message': 'List of Jobs', 'data': serializer})
            else:
                return Response({'message': 'No jobs listed..', 'data':[]})
            
        except Exception as e:
            return Response({'message':'failure','error': str(e)})
        