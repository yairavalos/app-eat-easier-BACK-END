# Standard Libraries and Packages:

from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class UnitsConvertion(models.Model):

    """
    Table of equivalencies between informal user types and Standard SI.

    Manager privileges needed to load this table through Admin interface
    """

    equivalency = models.CharField(max_length=50, unique=True)
    unit_value = models.FloatField()

    UNITS_DESC = (
        ('mililitros'),
        ('miligramos'),
        ('litros'),
        ('kilogramos'),
    )

    unit_desc = models.CharField(max_length=50, choices=UNITS_DESC)

    UNITS_TYPE = (
        ('custom'),
        ('SI'),
    )
    unit_type = models.CharField(max_length=50, choices=UNITS_TYPE)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.equivalency}'


class CatalogPackage(models.Model):

    """
    Table to refer to The Package´s Catalog

    Manager privileges needed to load this table through Admin interface
    """

    package_desc = models.CharField(max_length=50, unique=True)
    moq_value = models.FloatField()

    CONT_TYPE = (
        ('Wrapping'),
        ('Container'),
        ('Bulk'),
    )

    container_type = models.CharField()

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.package_desc}'


class CatalogIngredient(models.Model):

    """
    Table to represent The Ingredient´s Catalog used for Recipe´s Catalog and Supermarket Catalog

    Manager privileges needed to load this table through Admin interface
    """

    FOOD_TYPES = (
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

    ingredient_cat = models.CharField(max_length=100, choices=FOOD_TYPES)
    ingredient_name = models.CharField(max_length=100, unique=True)
    ingredient_cal = models.FloatField()

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.ingredient_name}'

class SprmktDept(models.Model):
 
    """
    Table to represent a Dictionary to set a classification on Super Market Deparment

    Manager privileges needed to load this table through Admin interface
    """

    category_desc = models.CharField(max_length=50, unique=True)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.category_desc}'


class SprmktPackaging(models.Model):
    
    """
    Table to represent The Supermarket´s Catalog

    Manager privileges needed to load this table through Admin interface
    """

    dept_id = models.ForeignKey(SprmktDept, on_delete=PROTECT,related_name='sprmkt_packs')
    ingredient_id = models.ForeignKey(CatalogIngredient, on_delete=PROTECT,related_name='sprmkt_packs')
    spq_value = models.IntegerField()
    unit_id = models.ForeignKey(UnitsConvertion, on_delete=PROTECT,related_name='sprmkt_packs')
    package_id = models.ForeignKey(CatalogPackage, on_delete=PROTECT,related_name='sprmkt_packs')

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.spq_value} {self.unit_id} {self.package_id}'


# Import between Apps
# Required to obtain menu id to link it to the Foreign Key
from App_User_Mgmt.models import UserMenu

class SprmktList(models.Model):

    """
    Table to cointaing The Results of Supermarket List Generations

    This table data its going to be loaded automatically by the business logic
    """

    menu_id = models.ForeignKey(UserMenu, on_delete=PROTECT,related_name='sprmkt_lists')
    qty = models.IntegerField()
    stock_id = models.ForeignKey(SprmktPackaging, on_delete=PROTECT,related_name='sprmkt_lists')

    # The following fields needs to be validated
    inventory = models.BooleanField(default=False)
    purchase = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.qty} {self.stock_id}'