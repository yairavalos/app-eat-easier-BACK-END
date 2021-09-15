# Standard Libraries and Packages:

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:
from App_User_Mgmt.serializers import UserSerializer

# Models:

# Create your views here.

class CoreAPIView(APIView):

    def get(self, request):
        return Response("This is Core Page View")

