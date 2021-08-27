# Standard Libraries and Packages:

from django.http import response
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:
from .serializers import CatalogRecipeSerializer

# Models:
from .models import CatalogRecipe

# Create your views here.
class RecipeAPIView(APIView):

    def get(self, request):
        return Response("This is Recipe Main View")


class RecipeListAPIView(generics.ListCreateAPIView):

    queryset = CatalogRecipe.objects.all()
    serializer_class = CatalogRecipeSerializer


