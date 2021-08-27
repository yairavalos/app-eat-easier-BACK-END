# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import RecipeAPIView, RecipeListAPIView, RecipeDetailsAPIView, RecipeDetailedViewerAPIView, RecipeIngredientListAPIView

app_name = "App_Recipe_Mgmt"

urlpatterns = [
    path('', RecipeListAPIView.as_view()),
    path('<int:pk>/', RecipeDetailsAPIView.as_view()),
    path('<int:pk>/viewer/',RecipeDetailedViewerAPIView.as_view()),
    path('ingredients/', RecipeIngredientListAPIView.as_view()),
]
