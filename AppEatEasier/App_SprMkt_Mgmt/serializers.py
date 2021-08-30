# Standard Libraries and Packages

from rest_framework import serializers

# Serializers
from App_User_Mgmt.serializers import UserPlannerListSerializer

# Models
from .models import SprmktList, SprmktPackaging, CatalogPackage, CatalogIngredient, UnitsConvertion


# Serializers Definition

class SprMktUnitConvertion(serializers.ModelSerializer):
    """
    This serializer help us to deal with Super Market Unit Types Convertion
    """

    class Meta:
        model = UnitsConvertion
        fields = ['equivalency']


class SprMktIngredientList(serializers.ModelSerializer):
    """
    This serializer help us to deal with Super Market Ingredients Catalog
    """

    class Meta:
        model = CatalogIngredient
        fields = ['ingredient_name']


class SprMktPacksListSerializer(serializers.ModelSerializer):
    """
    This serializer help us to deal with Super Market Packaging description
    """

    class Meta:
        model = CatalogPackage
        fields = ['package_desc']


class SprMktStockListSerializer(serializers.ModelSerializer):
    """
    This serializer help us to deal with Super Market Stock and Packaging Types
    """
    
    package_type = SprMktPacksListSerializer()
    ingredient = SprMktIngredientList()
    unit_type = SprMktUnitConvertion()

    class Meta:
        model = SprmktPackaging
        fields = ['package_type','spq_value','unit_type','ingredient','additional_desc']


class SprMktListSerializer(serializers.ModelSerializer):
    """
    This serializers help us to deal with User Planner Super Market List
    """
    
    user_planner = UserPlannerListSerializer()
    stock_package = SprMktStockListSerializer()

    class Meta:
        model = SprmktList
        fields = ['id','user_planner','qty','stock_package','purchase']