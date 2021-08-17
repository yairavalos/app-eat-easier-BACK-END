# Standard Libraries and Packages:

from django.db import models

# Create your models here.

class UnitsConvertion(models.Model):

    """
    Table of equivalencies between informal user types and Standard SI.

    Manager privileges needed to load this table through Admin interface
    """

    equivalency = models.CharField(max_length=50)
    unit_value = models.FloatField()

    UNITS_DESC = (
        ('mililitros'),
        ('miligramos'),
        ('litros'),
        ('kilogramos'),
    )

    unit_desc = models.CharField(max_length=50, choices=UNITS_DESC)

    UNITS_TYPE = (
        ('user'),
        ('SI'),
    )
    unit_type = models.CharField(max_length=50, choices=UNITS_TYPE)



class CatalogPackages(models.Model):

    """
    Table to refer to The Package´s Catalog

    Manager privileges needed to load this table through Admin interface
    """

    package_desc = models.CharField(max_length=50)
    moq_value = models.FloatField()

    CONT_TYPE = (
        ('envoltura'),
        ('contenedor'),
        ('granel'),
    )

    container_type = models.CharField()


class SprmktDept(models.Model):
 
    """
    Table to represent a Dictionary to set a classification on Super Market Deparment

    Manager privileges needed to load this table through Admin interface
    """

    category_desc = models.CharField(max_length=50)


class CatalogIngredients(models.Model):

    """
    Table to represent The Ingredient´s Catalog used for Recipe´s Catalog and Supermarket Catalog

    Manager privileges needed to load this table through Admin interface
    """

    INGREDIENT_TYPES = (
        ('Res'),
        ('Pollo'),
        ('Cerdo'),
        ('Pescado'),
        ('Huevo'),
        ('Lacteos'),
        ('Frutas'),
        ('Verduras'),
        ('Gluten'),
    )

    ingredient_cat = models.CharField(max_length=100, choices=INGREDIENT_TYPES)
    ingredient_name = models.CharField(max_length=100)
    ingredient_cal = models.FloatField()

class SprmktPackings(models.Model):
    
    """
    Table to represent The Supermarket´s Catalog

    Manager privileges needed to load this table through Admin interface
    """

    dept_id = models.ForeignKey()
    ingredient_id = models.ForeignKey()
    spq_value = models.IntegerField()
    units_id = models.ForeignKey()
    package_id = models.ForeignKey()


class SprmktList(models.Model):

    """
    Table to cointaing The Results of Supermarket List Generations

    This table data its going to be loaded automatically by the business logic
    """

    menu_id = models.ForeignKey()
    qty = models.IntegerField()
    stock_id = models.ForeignKey()

    # The following fields needs to be validated
    inventory = models.BooleanField()
    purchase = models.BooleanField()

