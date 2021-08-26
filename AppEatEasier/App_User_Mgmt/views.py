# Standard Libraries and Packages:

from rest_framework import generics, serializers, filters
from rest_framework.views import APIView
from rest_framework.response import Response

# Serializers:
from .serializers import (
    UserDetailSerializer, UserListSerializer, UserMenuListSerializer, 
    UserPlannerListSerializer, UserPlannerDetailSerializer, UserMenuDetailSerializer,
)

# Models:
from .models import User, UserMenu, UserPlanner

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
    # pk comes into the request layer and its injected into the queryset that match the criteria
    # lookup_field by default is pk
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserPlannerListAPIView(generics.ListAPIView):
    """
    This view its purpose its to list total User´s Planner
    """

    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerListSerializer


class UserPlannerIDListAPIView(generics.ListAPIView):
    """
    This view its purpose its to list specific User Planner by User ID 
    """

    # queryset = UserPlanner.objects.filter(user_profile_id='4') / this experiment works well
    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerListSerializer

    def get_queryset(self):
        user_profile_id = self.kwargs['pk']
        filters = {}

        if user_profile_id:
            filters['user_profile_id'] = user_profile_id

        return self.queryset.filter(**filters)


class UserPlannerIDDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view its purpose its to get a User Planner Detail by User ID
    """

    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerDetailSerializer

    def get_queryset(self):

        user_profile_id = self.kwargs['user_profile_id']
        plan_id = self.kwargs['pk']
        filters_dict = {}

        if user_profile_id:
            filters_dict['user_profile_id'] = user_profile_id
            filters_dict['id'] = plan_id

        return self.queryset.filter(**filters_dict)


class UerMenuListAPIView(generics.ListAPIView):
    """
    This views its purpose is to get a User Menu List by User Planner ID and User Profile ID 
    """
    #user_menu = UserMenu.objects.all().prefetch_related()

    queryset = UserMenu.objects.all()    
    serializer_class = UserMenuListSerializer
    # useful tool for debug -> print(str(queryset.query))
    
    def get_queryset(self):

        user_profile_id = self.kwargs['user_profile_id']
        plan_id = self.kwargs['pk']
        filters_dict = {}

        if plan_id:   
            filters_dict['user_planner_id'] = plan_id

        if user_profile_id:
            filters_dict['user_planner__user_profile_id'] = user_profile_id #the key its here !!!!

        return self.queryset.filter(**filters_dict)


class UserMenuIDDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view its purpose is to get a User Menu Item Detail by User Menu ID, User Planner ID and User Profile ID
    """

    queryset = UserMenu.objects.all()
    serializer_class = UserMenuDetailSerializer

    def get_queryset(self):

        user_profile_id = self.kwargs['user_profile_id']
        plan_id = self.kwargs['user_planner_id']
        menu_item = self.kwargs['pk']
        filters_dict = {}

        if plan_id:   
           filters_dict['user_planner_id'] = plan_id

        if user_profile_id:
           filters_dict['user_planner__user_profile_id'] = user_profile_id #the key its here !!!!

        if menu_item:
            filters_dict['pk'] = menu_item

        return self.queryset.filter(**filters_dict)
