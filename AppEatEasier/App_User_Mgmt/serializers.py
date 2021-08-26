# Standard Libraries and Packages

from rest_framework import serializers

# Models
from .models import User, UserProfile, UserFood, UserApp, UserRecipe, UserPlanner, UserMenu

# External Models
from App_Recipe_Mgmt.serializers import CatalogRecipeSerializer

# Serializers definition

class UserListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to bring Users List from DB
    """

    class Meta:
        model = User
        fields = ['id','username','email']


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
    #user_profile = serializers.StringRelatedField(many=False) # Interesting function, avoids to declare an extra serializer
    user_profile = UserListSerializer() 

    class Meta:
        model = UserProfile
        fields = ['user_profile','adults_qty','child_qty']


class UserProfileAppSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Appliances List)
    """
    user_profile = UserListSerializer() 

    class Meta:
        model = UserApp
        fields = ['user_profile','app_name']


class UserProfileFoodSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Food List)
    """
    user_profile = UserListSerializer() 

    class Meta:
        model = UserFood
        fields = ['user_profile','food_type']


class UserProfileRecipeSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to give the full User Profile including Preferences (Food List)
    """
    user_profile = UserListSerializer()
    cat_recipe = CatalogRecipeSerializer()

    class Meta:
        model = UserRecipe
        fields = ['user_profile','cat_recipe']
        depth = 1

class UserPlannerListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to List Users Planners
    """
    # OJO !!! hay usar los parentesis al final de la clase por favor !!!
    user_profile = UserListSerializer()

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


class UserMenuListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get User Menu according to a given User Planner ID
    """

    user_planner = UserPlannerListSerializer()

    class Meta:
        model = UserMenu
        fields = ['id','user_planner','meal_date','meal_type','user_recipe']


class UserRecipeListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get a Menu Item Detail by ID
    """

    class Meta:
        model = UserRecipe
        fields = ['id','cat_recipe']
        depth = 1


class UserMenuDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose is to get User Menu according to a given User Planner ID
    """

    user_planner = UserPlannerListSerializer()
    user_recipe = UserRecipeListSerializer()

    class Meta:
        model = UserMenu
        fields = ['id','user_planner','meal_date','meal_type','user_recipe','done']
