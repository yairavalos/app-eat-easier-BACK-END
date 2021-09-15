# Standard Libraries and Packages

from django.contrib import admin

# Register your models here.
from .models import ShoppingList, UnitsConvertion, CatalogIngredient, CatalogPackage, SprmktDept, SprmktPackaging, SprmktList

admin.site.register(UnitsConvertion)
admin.site.register(CatalogIngredient)
admin.site.register(ShoppingList)

# Reserved for the next version
# -------------------------------------------------
# admin.site.register(CatalogPackage)
# admin.site.register(SprmktDept)
# admin.site.register(SprmktPackaging)
# admin.site.register(SprmktList)

