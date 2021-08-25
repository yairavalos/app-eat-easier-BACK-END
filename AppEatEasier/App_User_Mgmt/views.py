# Standard Libraries and Packages:

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:
from .serializers import UserDetailSerializer, UserListSerializer, UserPlannerListSerializer

# Models:
from .models import User, UserPlanner

# Create your views here.

class UserAPIView(APIView):
    """
    This view its the first view from template for testing purposes
    """
    def get(self, request):
        return Response("This User Main Page View")


class UserListAPIView(generics.ListAPIView):
    """
    This view its purpose its to list total users into the system
    """

    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailsRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    This view its purpose its to retrieve full user details
    """

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserPlannerListAPIView(generics.ListAPIView):
    """
    This view its purpose its to list total User´s Planner
    """

    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerListSerializer

