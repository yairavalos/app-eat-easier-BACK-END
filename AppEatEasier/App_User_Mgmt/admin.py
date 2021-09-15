# Standard Libraries and Packages
from django.contrib import admin

# Register your models here.
from .models import UserProfile, UserFood, UserApp, UserRecipe, UserPlanner, UserMenu

admin.site.register(UserProfile)
admin.site.register(UserFood)
admin.site.register(UserApp)
admin.site.register(UserRecipe)
admin.site.register(UserPlanner)
admin.site.register(UserMenu)
