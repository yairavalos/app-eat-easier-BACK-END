# Standard Libraries and Packages

from django.db import models

# Create your models here.

class RecipeCategory(models.Model):

    """
    Table to represent The Catalog of different kind of recipes for their classification

    Manager privileges needed to load this table through Admin interface
    """

    category = models.CharField(max_length=150)


class CatalogRecipe(models.Model):

    """
    Table to contain The Main Catalog of Recipes

    Manager privileges needed to load this table through Admin interface
    """

    category_id = models.ForeignKey()
    title = models.CharField(max_length=150)

    MEAL_TYPES = (
        ('desayuno'),
        ('brunch'),
        ('comida'),
        ('merienda'),
        ('cena'),
    )

    meal_type = models.CharField(max_length=30, choices=MEAL_TYPES)
    description = models.TextField()
    n_eats = models.IntegerField()

    # This fields needs to be in minutes
    # Validate if doesn´t need to be into units convertion table
    time_prep = models.IntegerField()

    LEVEL_TYPES = (
        ('facil'),
        ('intermedio'),
        ('dificil'),
    )

    level_id = models.CharField(max_length=30, choices=LEVEL_TYPES)
    
    # Need to validate the field type in django
    pic_url = models.CharField()


class IngredientsRecipe(models.Model):

    """
    Table to contain the regarding Ingredients per Recipe

    Manager privileges needed to load this table through Admin interface
    """

    recipe_id = models.ForeignKey()
    ingredient_id = models.ForeignKey()
    ingredient_qty = models.FloatField()
    unit_id = models.ForeignKey()


class ProcedureRecipe(models.Model):

    """
    Table to contain the regarding step to process every Recipe

    Manager privileges needed to load this table through Admin interface
    """

    recipe_id = models.ForeignKey()
    proc_descrip = models.TextField()
    
    # Need to validate the field type in django
    pic_url = models.CharField()

