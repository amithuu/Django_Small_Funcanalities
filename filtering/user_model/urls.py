
from django.urls import path
from . import views


urlpatterns = [
    path('register', views.CustomUserCreateApiView.as_view(), name = 'register'),
    path('email_otp/request', views.EmailOtpRequestApiView.as_view(), name='email-otp-request'),
     path('email_otp/validate', views.EmailOtpValidateAPIView.as_view(), name='email-otp-request'),
]

