from django.urls import path
from . import views

urlpatterns = [
    path('linkedin', views.LinkedinAPIView.as_view(), name = 'linkedin_profile_api'),    
]

