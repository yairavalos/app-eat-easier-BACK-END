# Standard Libraries and Packages

from django.contrib import admin

# Register your models here.
from .models import UnitsConvertion, CatalogIngredient, CatalogPackage, SprmktDept, SprmktPackaging, SprmktList

admin.site.register(UnitsConvertion)
admin.site.register(CatalogIngredient)
admin.site.register(CatalogPackage)
admin.site.register(SprmktDept)
admin.site.register(SprmktPackaging)
admin.site.register(SprmktList)

