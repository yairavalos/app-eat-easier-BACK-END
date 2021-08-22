# Standard Libraries and Packages

from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class RecipeCategory(models.Model):

    """
    Table to represent The Catalog of different kind of recipes for their classification

    Manager privileges needed to load this table through Admin interface
    """

    # We need to validate this
    category = models.CharField(max_length=150, unique=True)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.category}'


class CatalogRecipe(models.Model):

    """
    Table to contain The Main Catalog of Recipes

    Manager privileges needed to load this table through Admin interface
    """

    recipe_category = models.ForeignKey(RecipeCategory, on_delete=PROTECT, related_name='recipes')
    title = models.CharField(max_length=150, unique=True)

    MEAL_TYPES = (
        ('desayuno','Desayuno'),
        ('brunch','Brunch'),
        ('comida','Comida'),
        ('merienda','Merienda'),
        ('cena','Cena'),
    )

    meal_type = models.CharField(max_length=30, choices=MEAL_TYPES)
    description = models.TextField()
    persons = models.IntegerField()

    # This fields needs to be in minutes
    # Validate if doesn´t need to be into units convertion table
    time_prep = models.IntegerField()

    LEVEL_TYPES = (
        ('alta','Alta'),
        ('media','Media'),
        ('baja','Baja'),
    )
    
    level = models.CharField(max_length=30, choices=LEVEL_TYPES)

    # Need to validate the field type in django
    pic_url = models.CharField(max_length=250)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.title}'


class RecipeApp(models.Model):

    """
    Table to contain the regarding appliances required to process the recipe

    Manager privileges needed to load this table through Admin Interface
    """

    cat_recipe = models.ForeignKey(CatalogRecipe, on_delete=PROTECT, related_name='recipe_apps')

    APPS_TYPES = (
        ('olla de presion','Olla de Presión'),
        ('licuadora','Licuadora'),
        ('microondas','Microondas'),
        ('horno','Horno'),
        ('procesador','Procesador'),
        ('estufa','Estufa'),
    )

    apps_type = models.CharField(max_length=30, choices=APPS_TYPES)
    apps_main = models.BooleanField(default=False)
    
    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.apps_name}'


# Import between Apps
# to relate Foreign Keys
from App_SprMkt_Mgmt.models import CatalogIngredient, UnitsConvertion

class RecipeIngredient(models.Model):

    """
    Table to contain the regarding Ingredients per Recipe

    Manager privileges needed to load this table through Admin interface
    """

    cat_recipe = models.ForeignKey(CatalogRecipe, on_delete=PROTECT,related_name='recipe_ingredients')
    cat_ingredient = models.ForeignKey(CatalogIngredient, on_delete=PROTECT,related_name='recipe_ingredients')
    ingredient_qty = models.FloatField()
    unit_type = models.ForeignKey(UnitsConvertion, on_delete=PROTECT, related_name='recipe_ingredients')

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.ingredient_id}'
 

class RecipeProcedure(models.Model):

    """
    Table to contain the regarding step to process every Recipe

    Manager privileges needed to load this table through Admin interface
    """

    cat_recipe = models.ForeignKey(CatalogRecipe, on_delete=PROTECT,related_name='recipe_procedures')
    proc_descrip = models.TextField()
    
    # Need to validate the field type in django
    pic_url = models.CharField(max_length=250)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.proc_descrip}'