# Standard Libraries and Packages

from django.contrib import admin

# Register your models here.
from .models import RecipeCategory, CatalogRecipe, RecipeApp, RecipeIngredient, RecipeProcedure

admin.site.register(RecipeCategory)
admin.site.register(CatalogRecipe)
admin.site.register(RecipeApp)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeProcedure)
