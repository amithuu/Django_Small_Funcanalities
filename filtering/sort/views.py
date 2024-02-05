from django.shortcuts import render

# Create your views here.
from sort import serializers 
from sort.models import Movie
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

class MovieCreateView(CreateAPIView):
    serializer_class = serializers.MovieSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        

# ?? One way of adding the filters to the attributes of the models.. and searching through parameters..
   
# class MovieListAPIView(ListAPIView):
#     serializer_class = MovieSerializer
    
#     def get(self, request, *args, **kwargs):
#         queryset = Movie.objects.all()
#         try:
#             name = self.request.query_params.get('name', None)
#             status = self.request.query_params.get('status', None)
            
#             if name:
#                 queryset = queryset.filter(movie_name__icontains = name)
            
#             if status:
#                 queryset = queryset.filter(movie_status = status)
                
            
#             serializer = self.get_serializer(queryset, many=True).data
            

#             if serializer:
#                 return Response({'message':'Success','data' : serializer})
#             else:
#                 return Response({'message':'No Data','data' : []})
                
#         except Exception as e:
#             return Response({'message':'Fail','data' : str(e)})

# ! If we haver more filters, then instead of over writing queryset again and again, we can use **kwargs and add it to one queryset..



# Todo: this view has an feature of saving the filtered search and filtering the data using the filters.. 
# ? The `MovieListAPIView` class is a view that retrieves a list of movies based on specified filters
# ? and returns the serialized data along with a saved URL for the search.

class MovieListAPIView(ListAPIView):
    serializer_class = serializers.MovieSerializer
    
    
    def get(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        try:
            parameter = {
                'name':'movie_name__icontains',
                'status': 'movie_status',
                'ranking': 'total_ratings',
                'created_year':'movie_created',
            }
            
            filters = {}
            
            for param, model_name in parameter.items():
                value = self.request.query_params.get(param, None) # ? status = self.request.query_params.get('status', None)
                if value:
                    filters[model_name] = value 
            
            queryset = queryset.filter(**filters)  # ? queryset = queryset.filter(movie_status = status)

            serializer = self.get_serializer(queryset, many=True).data
            
            return Response({'message':'Success', 'data':serializer})         
    

        except Exception as e:
            return Response({'message': 'Fail', "error": str(e)})

