# Standard Libraries and Packages:

from django.shortcuts import render
from rest_framework import generics

# Serializers:

# Models:

# Create your views here.

class CoreListAPIView(generics.ListCreateAPIView):
    pass