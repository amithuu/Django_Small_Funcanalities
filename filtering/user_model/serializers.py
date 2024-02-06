
from rest_framework import serializers
from .models import CustomerUser
from django.utils.text import slugify

class CustomerUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = CustomerUser
        fields = ['email', 'first_name', 'last_name', 'phone_number','password', 'confirm_password']
        
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
    
    