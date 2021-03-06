# Standard Libraries and Packages

from rest_framework import serializers

# Serializers
#from App_SprMkt_Mgmt.serializers import SprMktUnitConvertion

# Models
from .models import CatalogRecipe, RecipeApp, RecipeIngredient, RecipeProcedure
from App_SprMkt_Mgmt.models import UnitsConvertion

# Serializers definition

# ------------------------------------------------------------------------------------------------------------------------------------
#
# RECIPE MANAGEMENT SERIALIZERS
#
# ------------------------------------------------------------------------------------------------------------------------------------


class CatalogRecipeSerializer(serializers.ModelSerializer):
    """
    This serializer is going to help to bring the full List of recipes from Recipe´s Catalog 
    """

    class Meta:
        model = CatalogRecipe
        fields = ['id','recipe_category','title','meal_type','food_type','level','pic_url']
        depth = 1


class CatalogRecipeDetailsSerializer(serializers.ModelSerializer):
    """
    This serializer is going to help us bringing all details of a recipe from Recipe´s Catalog
    """

    class Meta:
        model = CatalogRecipe
        fields = ['id','recipe_category','title','meal_type','description','persons','time_prep','level','pic_url']
        depth = 1


class CatalogRecipeAppsSerializer(serializers.ModelSerializer):
    """
    This serializer is going to help us bringing the regarding Kitchen Appliances for a given Recipe
    """

    class Meta:
        model = RecipeApp
        fields = ['id','cat_recipe','apps_type','required']


class CatalogRecipeIngredientsSerializer(serializers.ModelSerializer):
    """
    This serializer is going to help us bringing the regarding Ingredients for a given Recipe
    """
    # Awesome if you just send the field name + _id you can just have that !! -> cat_recipe_id and you only get id !!
    class Meta:
        model = RecipeIngredient
        fields = ['id','cat_recipe_id','cat_ingredient','ingredient_qty','unit_type']
        depth = 1


class CatalogRecipeProcedureSerializer(serializers.ModelSerializer):
    """
    This serializer is going to help us bringing the regarding Cooking Procedure´s steps for a given Recipe
    """

    class Meta:
        model = RecipeProcedure
        fields = ['id','cat_recipe','proc_descrip','pic_url']



# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER PROFILED RECOMMENDATIONS / AUTOMATIC PROCESSING
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserSuggestionListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give a list of suggestions according with User´s Food Preferences
    """

    class Meta:
        model = CatalogRecipe
        fields = ['id','recipe_category','title','meal_type','level','pic_url']
        depth = 1

