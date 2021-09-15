# Standard Libraries and Packages

from django.db import models

# Import system models
from django.conf import global_settings # against documentation I had to use global_ in order to be able to found the AUTH_USER_MODEL
from django.contrib.auth.models import User # | abstract | extra queries to get user raw data | david feedback
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
    # user.settings must to be added
    #related name was missing
    # This field its sensitive, relation must be one to one from Auth User Table
    user_profile = models.OneToOneField(global_settings.AUTH_USER_MODEL, on_delete=PROTECT, related_name='user_profiles') 
    
    adults_qty = models.IntegerField()
    child_qty = models.IntegerField()
 
    # Some ideas to add and improve the profile
    # Some user logs
    # some stats

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.user_profile} | adult: {self.adults_qty} | child: {self.child_qty}' # validate if .username needs to be added


class UserFood(models.Model):

    """
    This table is going to cointain the user food preferences for search engine

    This table data its going to be loaded from the Front-End Side
    """

    user_profile = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=PROTECT,related_name='user_foods')
    
    FOOD_TYPES = (
        ('res','Res'),
        ('pollo','Pollo'),
        ('cerdo','Cerdo'),
        ('pescado','Pescado'),
        ('huevo','Huevo'),
        ('lacteos','Lacteos'),
        ('frutas','Frutas'),
        ('verduras','Verduras'),
        ('gluten','Gluten'),
    )

    food_type = models.CharField(max_length=30, choices=FOOD_TYPES)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'user: {self.user_profile} | food: {self.food_type}'


class UserApp(models.Model):

    """
    This table is going to cointain the user appliances into their Kitchen

    This table data its going to be loaded from the Front-End Side
    """

    user_profile = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=PROTECT,related_name='user_apps')
    
    APPS_TYPES = (
        ('olla de presion','Olla de Presión'),
        ('licuadora','Licuadora'),
        ('microondas','Microondas'),
        ('horno','Horno'),
        ('procesador','Procesador'),
        ('estufa','Estufa'),
    )
    
    app_name = models.CharField(max_length=30, choices=APPS_TYPES)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'user: {self.user_profile} | appliance: {self.app_name}'


# Import between Apps
# Needed to relate recipe id foreign key
from App_Recipe_Mgmt.models import CatalogRecipe

class UserRecipe(models.Model):

    """
    This table its going to contain the user recipes, by suggestion or by choice of the user

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    user_profile = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=PROTECT,related_name='user_recipes')
    cat_recipe = models.ForeignKey(CatalogRecipe, on_delete=PROTECT,related_name='user_recipes')
    checked = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'user: {self.user_profile} | recipe: {self.cat_recipe} | favorite:{self.favorite}'


class UserPlanner(models.Model):

    """
    Table to Generate the User Plan per Period

    This table data its going to be loaded from the Front-End Side
    """

    # This field its sensitive, relation must be one to one from Auth User Table
    user_profile = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=PROTECT,related_name='user_planners')
    plan_title = models.CharField(max_length=150)
    week_num = models.IntegerField()
    
    PERIOD_TYPES = (
        ('semanal','Semanal'),
        ('quincenal','Quincenal'),
    )
    
    period = models.CharField(max_length=30, choices=PERIOD_TYPES)
    
    start_date = models.DateField()
    end_date = models.DateField()

    # Confirmation from the user to save this plan for further reusability
    saved = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'user: {self.user_profile} | plan title: {self.plan_title} | start: {self.start_date} | end: {self.end_date}'


class UserMenu(models.Model):

    """
    Table to Generate the User Menu based on The Plan Id

    This table data its going to be loaded from the Front-End Side
    """

    user_planner = models.ForeignKey(UserPlanner, on_delete=PROTECT,related_name='user_menus')
    meal_date = models.DateField()

    MEAL_TYPES = (
        ('desayuno','Desayuno'),
        ('brunch','Brunch'),
        ('comida','Comida'),
        ('merienda','Merienda'),
        ('cena','Cena'),
    )

    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    user_recipe = models.ForeignKey(UserRecipe, on_delete=PROTECT,related_name='user_menus')
    
    # This field type needs to be validated
    done = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.user_planner} | meal date: {self.meal_date} | meal type: {self.meal_type} | {self.user_recipe}'
