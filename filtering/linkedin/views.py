from django.shortcuts import render
from rest_framework import generics
from linkedin.utils import Linkedin
from rest_framework.response import Response


# Create your views here.
class LinkedinAPIView(generics.ListAPIView):
    
    def get(self, request, *args, **kwargs):
        try:
            data = Linkedin.linkedin_api(self)
            return  Response({'message':'successfully fetched data from linkedin', 'data': data})

        except Exception as e:
            return  Response({'message':'Failed to fetched data from linkedin', 'error': str(e)})
            