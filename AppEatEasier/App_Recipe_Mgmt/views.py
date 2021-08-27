# Standard Libraries and Packages:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers:
from .serializers import CatalogRecipeSerializer

# Models:
from .models import CatalogRecipe

# Create your views here.
class RecipeAPIView(APIView):

    def get(self, request):
        return Response("This is Recipe Main View")


class RecipeListAPIView(generics.ListCreateAPIView):

    queryset = CatalogRecipe.objects.all()
    serializer_class = CatalogRecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','meal_type']

