
from django.contrib.auth.base_user import BaseUserManager

# ? this class is to manage the users, we are using our own user_manager to cerate the users..

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        
        if not email:
            raise ValueError('please provide the email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user        
    
    def create_superuser(self, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(email, password, **extra_fields)
    

        

    