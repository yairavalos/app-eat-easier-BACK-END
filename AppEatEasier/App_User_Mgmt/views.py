# Standard Libraries and Packages:

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:

# Models:

# Create your views here.

class UserAPIView(APIView):
    
    def get(self, request):
        return Response("This User Main Page View")

class UserListAPIView(generics.ListCreateAPIView):
    pass