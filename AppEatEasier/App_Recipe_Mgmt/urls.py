# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import RecipeAPIView, RecipeListAPIView, RecipeDetailsAPIView

app_name = "App_Recipe_Mgmt"

urlpatterns = [
    path('', RecipeListAPIView.as_view()),
    path('<int:pk>/', RecipeDetailsAPIView.as_view()),
]
