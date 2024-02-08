from django.shortcuts import render
from .models import CustomerUser, OtpLog
from . import serializers
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView, CreateAPIView
from rest_framework.validators import ValidationError
from filtering.helpers import  send_otp_email
from rest_framework_simplejwt.tokens import RefreshToken  # for register and login to check the login..
from django.contrib.auth import authenticate # for login..
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
            user = serializer.instance
            
            refresh = RefreshToken.for_user(user)
            
            data = {}
            data['id'] = user.id
            data['token'] = {
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }
            
            return Response({'data':data})
        
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
    


class LoginAPIView(CreateAPIView):
    serializer_class = serializers.LoginSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data = request.data)
            
            if not serializer.is_valid(raise_exception=True):
                return ValidationError('login already exists')
            
            # email = serializer.data['email']
            # password = serializer.data['password']
            data = serializer.data
            user = authenticate(**data)
            
            # ? if you use validate in serializer then use this here..
            # user = serializer.data
            
            refresh = RefreshToken.for_user(user)

            data = {}
            
            data['id']=user.id
            data['token'] = {
                'refresh':str(refresh),
                'access_token':str(refresh.access_token),
            }
            
            return Response({'data':data})

        except Exception as e:
            return Response({"error": str(e)})
        
from rest_framework.permissions import AllowAny, IsAuthenticated
class LogoutAPiView(CreateAPIView):
    
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token).blacklist()
            
            return Response({"Logout":'Successfully Logged out'})
        
        except Exception as e:
            return Response({
                "detail": "Given token not valid for any token type",
                "code": "token_not_valid",
                "messages": [
                    {
                        "token_class": "AccessToken",
                        "token_type": "access",
                        "message": "Token is invalid or expired"
                    }
                ]
})

# ! Need to pass [access_token] in Bearer and [refresh_token] in Body.. 
