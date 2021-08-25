# Standard Libraries and Packages

from django.db import models
from rest_framework import serializers
from .models import User, UserProfile, UserFood, UserApp, UserRecipe, UserPlanner, UserMenu

# Serializers definition

class UserListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to bring Users List from DB
    """

    class Meta:
        model = User
        fields = ['id','username','email']


class UserDetailSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to bring User Detail from DB
    """

    class Meta:
        model = User
        fields = ['id','username','email','first_name','last_name','is_active','is_superuser']


class UserPlannerListSerializer(serializers.ModelSerializer):
    """
    This serializer its purpose its to List Users Planners
    """
    # OJO !!! hay usar los parentesis al final de la clase por favor !!!
    user_profile = UserListSerializer()

    class Meta:
        model = UserPlanner
        fields = ['user_profile','id','plan_title','period','start_date']