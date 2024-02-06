from django.shortcuts import render
from .models import CustomerUser
from . import serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.validators import ValidationError
# Create your views here.


class CustomUserCreateApiView(ListCreateAPIView):
    serializer_class=serializers.CustomerUserSerializer
    
    def post(self, request,*args,**kwargs):
        try:
            serializer = self.get_serializer(data = request.data)
            
            if not serializer.is_valid(raise_exception=True):
                return ValidationError(serializer.errors)
            
            serializer.save()
            return Response({'data':serializer.data})
        
        except Exception as e:
            return Response({'error':str(e)})
            
            
            
    def get(self, request,*args,**kwargs):
        queryset = CustomerUser.objects.all()
        
        try:
            serializer = self.get_serializer(queryset, many=True).data
            return Response({'data':serializer})
        
        except Exception as e:
            return Response({'error':str(e)})
    