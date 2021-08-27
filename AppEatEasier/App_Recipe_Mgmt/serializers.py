# Standard Libraries and Packages

from rest_framework import serializers

# Models
from .models import CatalogRecipe

# Serializers definition

class CatalogRecipeSerializer(serializers.ModelSerializer):
    """
    This serializers is going to help to bring the full List of recipes from Recipe´s Catalog 
    """

    class Meta:
        model = CatalogRecipe
        fields = ['id','recipe_category','title','meal_type']
        depth = 1

