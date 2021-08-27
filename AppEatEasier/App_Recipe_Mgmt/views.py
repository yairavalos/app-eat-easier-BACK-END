# Standard Libraries and Packages:

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# Serializers:
from .serializers import (
    CatalogRecipeAppsSerializer, CatalogRecipeSerializer, 
    CatalogRecipeDetailsSerializer, CatalogRecipeIngredientsSerializer,
    CatalogRecipeProcedureSerializer,
)

# Models:
from .models import CatalogRecipe, RecipeApp, RecipeIngredient, RecipeProcedure

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


class RecipeDetailedViewerAPIView(generics.ListAPIView):
    """
    This views brings 4 different models in just one view to create The Recipe Viewer
    """

    #queryset = CatalogRecipe.objects.all()
    #serializer_class = CatalogRecipeDetailsSerializer

    def get_queryset(self):
        recipe_id = self.kwargs['pk']
        filter = {}
        
        if recipe_id:
            filter['id'] = recipe_id

        return CatalogRecipe.objects.filter(**filter)

    def get_queryset_apps(self):
        recipe_id = self.kwargs['pk']
        filter = {}
        
        if recipe_id:
            filter['cat_recipe_id'] = recipe_id

        return RecipeApp.objects.filter(**filter)
    
    def get_queryset_ingredients(self):
        recipe_id = self.kwargs['pk']
        filter = {}
        
        if recipe_id:
            filter['cat_recipe_id'] = recipe_id

        return RecipeIngredient.objects.filter(**filter)

    def get_queryset_procedure(self):
        recipe_id = self.kwargs['pk']
        filter = {}
        
        if recipe_id:
            filter['cat_recipe_id'] = recipe_id

        return RecipeProcedure.objects.filter(**filter)

    def list(self, request, *args, **kwargs):
        recipe_details = CatalogRecipeDetailsSerializer(self.get_queryset(), many=True)
        recipe_apps = CatalogRecipeAppsSerializer(self.get_queryset_apps(), many=True)
        recipe_ingredients = CatalogRecipeIngredientsSerializer(self.get_queryset_ingredients(), many=True) 
        recipe_procedure = CatalogRecipeProcedureSerializer(self.get_queryset_procedure(), many=True)
        
        return Response(
            {
                "recipe_details": recipe_details.data,
                "recipe_apps": recipe_apps.data,
                "recipe_ingredients": recipe_ingredients.data,
                "recipe_procedure": recipe_procedure.data
            }
        )
