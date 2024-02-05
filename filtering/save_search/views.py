from django.shortcuts import render
from django.contrib.auth.models import User
from save_search.models import Cricketer, Saved_Search
from save_search import serializers
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.validators import ValidationError
# Create your views here.


# The CricketerCreateAPIView class is a view that handles the creation of a Cricketer object using a
# POST request.
class CricketerCreateAPIView(ListAPIView):
    serializer_class = serializers.Cricketer_Serializer
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data = request.data)

            if not serializer.is_valid(raise_exception=False):
                return Response(ValidationError)
            
            serializer.save()
            return Response({'message': 'Successfully created Cricketer', 'data': serializer.data})
        
        except Exception as e:
            return Response({'Error': str(e)})
                

# The `CricketerListAPIView` class is a view that retrieves a list of cricketers based on specified
# filters and returns the serialized data.
class CricketerListAPIView(ListAPIView):
    serializer_class  =serializers.Cricketer_Serializer
    
    def get(self, request, *args, **kwargs):
        try:
            # adding filters
            param = {
                'name':'name__icontains',
                'role':'role__icontains',
            }
            
            filters={}
            
            for param, model_name in param.items():
                value = self.request.query_params.get(param,None)
                if value:
                    filters[model_name]= value
        
            # queryset = Cricketer.objects.filter(**filters)   
                
            serializer = self.get_serializer( Cricketer.objects.filter(**filters) , many=True).data
            
            if serializer:
                return Response({'message': 'Data Retrieved', 'data': serializer})
            else:
                return Response({'message': 'No Data Retrieved', 'data': []})
                
        except Exception as e:
            return Response({'Error': str(e)})


# The `SaveUrlAPIView` class is a view in a Django REST framework API that retrieves data from the
# `Cricketer` model based on filters provided in the URL parameters, saves the URL with the filters in
# the `Saved_Search` model, and returns the serialized data.
class SaveUrlAPIView(ListAPIView):
    serializer_class  =serializers.Cricketer_Serializer
    
    def get(self, request, *args, **kwargs):
        try:
            # adding filters
            param = {
                'name':'name__icontains',
                'role':'role__icontains',
            }
            
            filters={}
            save = {}
            
            for param, model_name in param.items():
                value = self.request.query_params.get(param,None)
                if value:
                    filters[model_name]= value
                    save[param] = value

            
            user = User.objects.get(username = 'amith')   
            # The code `url = f'http://127.0.0.1:8000/filter?' + '&'.join([f'{param}:{value}' for
            # param,value in save.items()])` is creating a URL string that will be saved in the
            # `Saved_Search` model.
            url = f'http://127.0.0.1:8000/filter?' + '&'.join([f'{param}:{value}' for param,value in save.items()])
            
            Saved_Search.objects.create(user=user,saved = url) # ? no need to store in any var..
            
                
            # queryset = Cricketer.objects.filter(**filters)
            serializer = self.get_serializer( Cricketer.objects.filter(**filters) , many=True).data
            
            if serializer:
                return Response({'message': 'Data Retrieved', 'data': serializer})
            else:
                return Response({'message': 'No Data Retrieved', 'data': []})
                
        except Exception as e:
            return Response({'Error': str(e)})



# The `Saved_SearchAPIView` class is a view that retrieves saved searches for a specific user and
# returns the data in a serialized format.
class Saved_SearchAPIView(ListAPIView):
    serializer_class = serializers.Saved_Serializer
    
    def get(self, request, *args, **kwargs):
        try:
            user=self.request.query_params.get('user',None)
                  
            serializer = self.get_serializer(Saved_Search.objects.filter(user=user), many=True).data
            
            if serializer:
                return Response({'message':'Successful', 'data':serializer})
            else:
                return Response({'message': 'No Data Retrieved', 'data': []})
                    
        except Exception as e:
            return Response({'message':'Error', 'error': str(e)})
            
    