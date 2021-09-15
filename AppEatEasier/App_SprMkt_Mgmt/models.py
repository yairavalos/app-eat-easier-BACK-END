# Standard Libraries and Packages:

from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

# ------------------------------------------------------------------------------------------------------------------------------------
#
# CURRENT VERSION SIMPLE MARKET SHOPPING LIST
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UnitsConvertion(models.Model):

    """
    Table of equivalencies between informal user types and Standard SI.

    Manager privileges needed to load this table through Admin interface
    """

    equivalency = models.CharField(max_length=50, unique=True)
    unit_value = models.FloatField()

    UNITS_DESC = (
        ('ml','mililitros'),
        ('gm','gramos'),
        ('l','litros'),
        ('kg','kilogramos'),
    )

    unit_desc = models.CharField(max_length=50, choices=UNITS_DESC)

    UNITS_TYPE = (
        ('user','Informal por convención entre usuarios'),
        ('custom','sugerida por al app, bajo revisión'),
        ('SI','Sistema Internacional de Unidades'),
    )
    unit_type = models.CharField(max_length=50, choices=UNITS_TYPE)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.equivalency}'


# Maybe is better just add a field -> Type of distribution -> Bulk / Packing / Piece
class CatalogIngredient(models.Model):

    """
    Table to represent The Ingredient´s Catalog used for Recipe´s Catalog and Supermarket Catalog

    Manager privileges needed to load this table through Admin interface
    """

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
        ('gluten free','Sin Gluten'),
        ('cereales, semillas y leguminosas','Cereales, Semillas y Leguminosas'),
        ('especias, condimentos y salsas','Especias, Condimentos y Salsas'),
    )

    ingredient_cat = models.CharField(max_length=100, choices=FOOD_TYPES)
    ingredient_name = models.CharField(max_length=100, unique=True)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.ingredient_name}'


# Import between Apps
# Required to obtain menu id to link it to the Foreign Key
from App_User_Mgmt.models import UserPlanner


# New Table to Generate Super Market List
# ------------------------------------------------------------------------------------------
class ShoppingList(models.Model):
    """
    Table to Dump the Shopping List Results
    """

    user_planner = models.ForeignKey(UserPlanner, on_delete=PROTECT, related_name='shopping_lists')
    ingredient_qty = models.FloatField()
    
    UNITS_DESC = (
        ('ml','mililitros'),
        ('gm','gramos'),
        ('l','litros'),
        ('kg','kilogramos'),
    )
    unit_desc = models.CharField(max_length=50, choices=UNITS_DESC)
    
    ingredient = models.ForeignKey(CatalogIngredient, on_delete=PROTECT, related_name='shopping_lists')
    check = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.user_planner} {self.ingredient_qty} {self.unit_desc} de {self.ingredient}'



# ------------------------------------------------------------------------------------------------------------------------------------
#
# NEXT VERSION WITH SUPERMARKET API CONNECTION
#
# ------------------------------------------------------------------------------------------------------------------------------------

class CatalogPackage(models.Model):

    """
    Table to refer to The Package´s Catalog

    Manager privileges needed to load this table through Admin interface
    """

    package_desc = models.CharField(max_length=50, unique=True)
    moq_value = models.FloatField()

    CONT_TYPE = (
        ('pack','Package'),
        ('container','Container'),
        ('bulk','Bulk'),
    )

    container_type = models.CharField(max_length=30, choices=CONT_TYPE)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.package_desc}'


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

    department = models.ForeignKey(SprmktDept, on_delete=PROTECT,related_name='sprmkt_packs')
    ingredient = models.ForeignKey(CatalogIngredient, on_delete=PROTECT,related_name='sprmkt_packs')
    
    # This field its added to make sense the ingredient status
    # por ejemplo, papas a la francesa, pimienta molida
    # additional description -> a la francesa (cortado & frito), molido o en polvo, en gajos, en grano o en rajas, etc.
    # This field its optional, but sometime needed to make sense lexically speaking
    additional_desc = models.CharField(max_length=150, blank=True)

    spq_value = models.FloatField()
    unit_type = models.ForeignKey(UnitsConvertion, on_delete=PROTECT,related_name='sprmkt_packs')
    package_type = models.ForeignKey(CatalogPackage, on_delete=PROTECT,related_name='sprmkt_packs')

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.ingredient} {self.additional_desc} {self.package_type} de {self.spq_value} {self.unit_type}'


class SprmktList(models.Model):

    """
    Table to cointaing The Results of Supermarket List Generations

    This table data its going to be loaded automatically by the business logic
    """

    user_planner = models.ForeignKey(UserPlanner, on_delete=PROTECT,related_name='sprmkt_lists')
    qty = models.IntegerField()
    stock_package = models.ForeignKey(SprmktPackaging, on_delete=PROTECT,related_name='sprmkt_lists')

    # The following fields needs to be validated
    inventory = models.BooleanField(default=False)
    purchase = models.BooleanField(default=False)

    # String function to get a readable object description
    def __str__(self) -> str:
        return f'{self.user_planner} | {self.qty} {self.stock_package}'