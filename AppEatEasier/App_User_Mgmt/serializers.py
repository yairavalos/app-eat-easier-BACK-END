# Standard Libraries and Packages

from django.db import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

# Models
from .models import User, UserProfile, UserFood, UserApp, UserRecipe, UserPlanner, UserMenu

# External Models
from App_Recipe_Mgmt.serializers import CatalogRecipeSerializer

# Serializers definition
class UserSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to generate new user through sign-up view
    """

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to bring Users List from DB
    """

    class Meta:
        model = User
        fields = ['id','username'] # ,'email' has been removed in order to be more dynamic on data exchange


class UserDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to bring User Detail from DB
    """

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','is_active','is_superuser']


class UserProfileSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (# of persons)
    """
    
    user_profile = UserListSerializer() 

    class Meta:
        model = UserProfile
        fields = ['id','user_profile','adults_qty','child_qty']


class UserProfilePeopleQtySerializer(serializers.ModelSerializer): # Designed for POST
    """
    This serializer its purpose is to give the full User Profile including Preferences (# of persons)
    """

    class Meta:
        model = UserProfile
        fields = ['user_profile','adults_qty','child_qty'] # 'id',

    def create(self, request): # request => json -> print()
        print(request['user_profile'])
        user_people = UserProfile.objects.create(user_profile=request['user_profile'], adults_qty=request['adults_qty'], child_qty=request['child_qty'])
        return user_people
        


class UserProfileAppSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Appliances List)
    """
    user_profile = UserListSerializer() 

    class Meta:
        model = UserApp
        fields = ['id','user_profile','app_name']


class UserProfileEditAppsSerializer(serializers.ModelSerializer): # Designed for POST
    """
    This serializer its purpose is to POST User´s Kitchen Appliances
    """

    class Meta:
        model = UserApp
        fields = ['user_profile', 'app_name']

    def create(self, validated_data):
        print(validated_data)
        user_apps = UserApp.objects.create(**validated_data)
        return user_apps


class UserProfileFoodSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Food List)
    """
    user_profile = UserListSerializer() 

    class Meta:
        model = UserFood
        fields = ['id','user_profile','food_type']


class UserProfileEditFoodSerializer(serializers.ModelSerializer): # Designed for POST
    """
    This serializer its purpose is to POST User´s Food Preferences 
    """

    class Meta:
        model = UserFood
        fields = ['user_profile', 'food_type']

    def create(self, validated_data):
        print(validated_data)
        user_food = UserFood.objects.create(**validated_data)
        return user_food

class UserProfileRecipeSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Food List)
    """
    user_profile = UserListSerializer()
    cat_recipe = CatalogRecipeSerializer()

    class Meta:
        model = UserRecipe
        fields = ['id','user_profile','cat_recipe']
        depth = 1


class UserFavoritesListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the List of User´s Favorites Recipes
    """

    user_profile = UserListSerializer()
    cat_recipe = CatalogRecipeSerializer()

    class Meta:
        model = UserRecipe
        fields = ['id','user_profile','cat_recipe','checked','favorite']
        depth = 1


class UserPlannerListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to List Users Planners
    """
    # OJO !!! hay usar los parentesis al final de la clase por favor !!!
    user_profile = UserListSerializer() #-> this can be optional or make an other serializer for retrieve - POST doesn´t need it
                                            # because it´s going to try to create a new user as well
    class Meta:
        model = UserPlanner
        fields = ['id','user_profile','plan_title','period','start_date']


class UserPlannerDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to get User Planner Details
    """

    user_profile = UserListSerializer()

    class Meta:
        model = UserPlanner
        fields = ['id','user_profile','plan_title','week_num','period','start_date','end_date','saved']


class UserPlannerCreateDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to get User Planner Details
    """

    class Meta:
        model = UserPlanner
        fields = ['id','user_profile','plan_title','week_num','period','start_date','end_date','saved']


class UserRecipeListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get a Menu Item Lists by ID
    """

    class Meta:
        model = UserRecipe
        fields = ['id','cat_recipe_id']


class UserRecipeDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get a Menu Item Detail by ID
    """

    class Meta:
        model = UserRecipe
        fields = ['id','cat_recipe','favorite']
        depth = 1


class UserMenuListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get User Menu according to a given User Planner ID
    """

    user_planner = UserPlannerListSerializer()
    user_recipe = UserRecipeDetailSerializer()

    class Meta:
        model = UserMenu
        fields = ['id','user_planner','meal_date','meal_type','user_recipe']


class UserMenuDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get User Menu according to a given User Planner ID
    """

    user_planner = UserPlannerListSerializer()
    user_recipe = UserRecipeDetailSerializer()

    class Meta:
        model = UserMenu
        fields = ['id','user_planner','meal_date','meal_type','user_recipe','done']
