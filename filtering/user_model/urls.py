
from django.urls import path
from . import views


urlpatterns = [
    path('register', views.CustomUserCreateApiView.as_view(), name = 'register'),
    path('',views.home),
    path('logout', views.logout_view)
]

