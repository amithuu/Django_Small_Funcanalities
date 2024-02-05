from django.urls import path
from save_search import views

urlpatterns = [
    path('cricketer',views.CricketerCreateAPIView.as_view(), name = 'save_cricket'),
    path('cricketer_list', views.CricketerListAPIView.as_view(), name = 'save_cricket_list'),
    path('save_url', views.SaveUrlAPIView.as_view(), name = 'save_url'),
    path('saved_list', views.Saved_SearchAPIView.as_view(), name = 'save_search'),
]
