# Standard Libraries and Packages

from django.db import models

# Import system models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT

# Create your models here.

class UserProfile(models.Model):
    
    """
    !!! WARNING !!!!

    This class needs to be reviewed in order to be aligned with Auth User Table from Django,
    Security needs to be aligned in this table

    Table to save the User Preferences onces is logged into the System

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    user_id = models.OneToOneField(User, on_delete=PROTECT)

    adults_qty = models.IntegerField()
    child_qty = models.IntegerField()
    
    # This field type needs to be validated
    food_list = models.JSONField()
    apps_list = models.JSONField()

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.user_id}'


# Import between Apps
# Needed to relate recipe id foreign key
from App_Recipe_Mgmt.models import CatalogRecipe

class UserRecipe(models.Model):

    """
    This table its going to contain the user recipes, by suggestion or by choice of the user

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    profile_id = models.ForeignKey(UserProfile, related_name='user_recipes')
    recipe_id = models.ForeignKey(CatalogRecipe, related_name='user_recipes')
    checked = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.preference_id} {self.recipe_id}'


class UserPlanner(models.Model):

    """
    Table to Generate the User Plan per Period

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    profile_id = models.ForeignKey(UserProfile, related_name='user_planners')
    plan_title = models.CharField(max_length=150, unique=True)
    week_num = models.IntegerField()
    
    PERIOD_TYPES = (
        ('semanal'),
        ('quincenal'),
    )
    
    period = models.CharField(max_length=30, choices=PERIOD_TYPES)
    
    start_date = models.DateField()
    end_date = models.DateField()

    # Confirmation from the user to save this plan for further reusability
    saved = models.CharField()

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.plan_title}'


class UserMenu(models.Model):

    """
    Table to Generate the User Menu based on The Plan Id

    This table data its going to be loaded from the Front-End Side
    """

    planner_id = models.ForeignKey(UserPlanner, related_name='user_menus')
    meal_date = models.DateField()

    MEAL_TYPES = (
        ('desayuno'),
        ('brunch'),
        ('comida'),
        ('merienda'),
        ('cena'),
    )

    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    user_recipe_id = models.ForeignKey(UserRecipe, related_name='user_menus')
    
    # This field type needs to be validated
    done = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.planner_id} {self.meal_date} {self.meal_type}'
