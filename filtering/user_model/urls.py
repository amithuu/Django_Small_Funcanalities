
from django.urls import path
from . import views


urlpatterns = [
    path('register', views.CustomUserCreateApiView.as_view(), name = 'register'),
    path('email_otp/request', views.EmailOtpRequestApiView.as_view(), name='email-otp-request'),
    path('email_otp/validate', views.EmailOtpValidateAPIView.as_view(), name='email-otp-request'),
    path('login', views.LoginAPIView.as_view(), name = 'login'),
    path('logout', views.LogoutAPiView.as_view(), name = 'logout'),
    path('password_change', views.PasswordChangeAPiView.as_view(), name = 'password_change'),
    
    path('forget_password/otp_request', views.ForgetPasswordOtpApiView.as_view(), name = 'forget_password'),
    path('forget_password/validate', views.ForgetPasswordOtpValidateAPIView.as_view(), name = 'forget_password_validate'),
    path('change_password',  views.ChangePasswordOtpValidateAPiView.as_view(), name = 'change_password'),
    
    path('user_profile', views.ProfileAPiView.as_view(), name = 'user_profile'),
]