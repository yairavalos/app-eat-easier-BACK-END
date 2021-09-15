# Standard Libraries and Packages:

from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:
from .serializers import SprMktListSerializer

# Models:
from .models import SprmktList

# Create your views here.
class SprMktAPIView(APIView):

    def get(self, request):
        return Response("This Super Market Main View")


class SprMktListAPIView(generics.ListAPIView):
    """
    This views its purpose is to bring and show a specific shopping list from Super Market
    """

    queryset = SprmktList.objects.all()
    serializer_class = SprMktListSerializer

    def get_queryset(self):

        user_profile_id = self.kwargs['user_profile_id']
        plan_id = self.kwargs['user_planner_id']
        filters_dict = {}

        if plan_id:   
           filters_dict['user_planner_id'] = plan_id

        if user_profile_id:
           filters_dict['user_planner__user_profile_id'] = user_profile_id #the key its here !!!!

        return self.queryset.filter(**filters_dict)
