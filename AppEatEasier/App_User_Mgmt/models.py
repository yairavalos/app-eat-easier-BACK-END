# Standard Libraries and Packages

from django.db import models

# Create your models here.

class UserPreferences(models.Model):
    
    """
    !!! WARNING !!!!

    This class needs to be reviewed in order to be aligned with Auth User from Django
    Security needs to be aligned in this table

    Table to save the User Preferences onces is logged into the System

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    user_id = models.OneToOneField

    adults_qty = models.IntegerField()
    child_qty = models.IntegerField()
    
    # This field type needs to be validated
    food_list = models.JSONField()
    apps_list = models.JSONField()


class UserRecipes(models.Model):

    """
    This table its going to contain the user recipes, by suggestion or by choice of the user

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    preference_id = models.ForeignKey()
    recipe_id = models.ForeignKey()
    checked = models.BooleanField()
    favorite = models.BooleanField()


class UserPlanner(models.Model):

    """
    Table to Generate the User Plan per Period

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    preference_id = models.ForeignKey()
    plan_title = models.CharField()
    week_num = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    PERIOD_TYPES = (
        ('semanal'),
        ('quincenal'),
    )
    
    period = models.CharField(max_length=30, choices=PERIOD_TYPES)
    save = models.CharField()


class UserMenu(models.Model):

    """
    Table to Generate the User Menu based on The Plan Id

    This table data its going to be loaded from the Front-End Side
    """

    planner_id = models.ForeignKey()
    meal_date = models.DateField()
    meal_type = models.CharField()
    user_recipe_id = models.ForeignKey()
    
    # This field type needs to be validated
    done = models.BooleanField()
