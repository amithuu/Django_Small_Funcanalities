
from rest_framework import serializers
from .models import CustomerUser, OtpLog
from django.utils.text import slugify
from rest_framework.validators import ValidationError 
class CustomerUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField()
    otp = serializers.IntegerField()
    class Meta:
        model = CustomerUser
        fields = ['email', 'first_name', 'last_name', 'phone_number','password', 'confirm_password','token','otp']
        
        # as we dont want to show in User Details..
        extra_kwargs={
            'password':{'write_only':True},
            'confirm_password':{'write_only':True},
        }

    def validate(self, value):
        
        if value['password']!=value['confirm_password']:
            raise serializers.ValidationError('Password and confirm password should be same.. ')
        
        if len(str(value['phone_number'])) < 10:
            raise serializers.ValidationError('invalid mobile number')
        del value['confirm_password']
        
        return value
    
    def generate_unique_username(self, email):
        unique_username = slugify(email)
        num=1
        while CustomerUser.objects.filter(username = unique_username).exists():
            unique_username = '{}-{}'.format(unique_username, num)
            num +=1
        return unique_username
    
    
    def create(self, validated_data):
        validated_data['username'] = self.generate_unique_username(validated_data['email'])
        return CustomerUser.objects.create_user(**validated_data)
    
    
    
class EmailOtpRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtpLog
        fields = ['email',]
        
class EmailOtpValidateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OtpLog
        fields = ['email','token','otp']
        
    def validate(self, value):
        if len(str(value))!= 6:
            raise ValidationError('please enter correct otp')

        return value
    
    def validate(self, value):
        otp_log = OtpLog.objects.filter(
            type='email_otp', email=value['email'],token = value['token'], otp=value['otp']
        ).exists()
        
        if not otp_log:
            raise ValidationError('invalid otp')
        return value
