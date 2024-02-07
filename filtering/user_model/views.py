from django.shortcuts import render
from .models import CustomerUser, OtpLog
from . import serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.validators import ValidationError
from filtering.helpers import  send_otp_email
# from rest_framework.simplejwt.token import RefreshToken
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

class CustomUserCreateApiView(ListCreateAPIView):
    serializer_class=serializers.CustomerUserSerializer
    
    def post(self, request,*args,**kwargs):
        try:
            serializer = self.get_serializer(data = request.data)
            
            if not serializer.is_valid(raise_exception=True):
                return ValidationError(serializer.errors)
            
            
            serializer.save()
            # data = serializer.data
            # data={}
            # data['token'] =  
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
    

class EmailOtpRequestApiView(CreateAPIView):
    serializer_class = serializers.EmailOtpRequestSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid(raise_exception=False):
            return ValidationError(serializer.errors)
        
        data = serializer.validated_data
        
        token_otp = send_otp_email(data.get('email'))

        if token_otp['token']==None and token_otp['otp']==None:
            return Response({'error':'token not received'}
                            )   
                 
        return Response({'Token_Otp':token_otp})
    

    
class EmailOtpValidateAPIView(CreateAPIView):
    serializer_class = serializers.EmailOtpValidateSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid(raise_exception=False):
            return ValidationError(serializer.errors)
        
        return Response({'ok':'ok'})
    
    