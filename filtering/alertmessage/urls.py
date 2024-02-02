from django.urls import path
from . import views


urlpatterns = [
    path('job_create',views.JobCreateAPIView.as_view(), name = 'job_create'),
    path('job_list', views.JobListAPIView.as_view(), name='job_list'),
]
