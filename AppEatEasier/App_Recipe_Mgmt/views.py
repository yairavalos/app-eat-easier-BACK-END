# Standard Libraries and Packages:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers:
from .serializers import CatalogRecipeSerializer, CatalogRecipeDetailsSerializer

# Models:
from .models import CatalogRecipe

# Create your views here.
class RecipeAPIView(APIView):

    def get(self, request):
        return Response("This is Recipe Main View")


class RecipeListAPIView(generics.ListCreateAPIView):
    """
    This View brings a list of recipes from Recipe´s Catalog
    """

    queryset = CatalogRecipe.objects.all()
    serializer_class = CatalogRecipeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title','meal_type','recipe_category__category'] #this kind of chaining its awesome !!!!
    ordering_fields = ['recipe_category']


class RecipeDetailsAPIView(generics.ListCreateAPIView):
    """
    This view brings a recipe details from Recipe´s Catalog
    """

    queryset = CatalogRecipe.objects.all()
    serializer_class = CatalogRecipeDetailsSerializer

    def get_queryset(self):

        recipe_id = self.kwargs['pk']
        filter = {}

        if recipe_id:
            filter['id'] = recipe_id

        return CatalogRecipe.objects.filter(**filter)