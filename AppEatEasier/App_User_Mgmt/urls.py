# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# External Views
from App_SprMkt_Mgmt.views import SprMktListAPIView

# Views:
from .views import (
    UserAPIView, UserListAPIView, UserDetailsRetrieveUpdateAPIView, 
    UserPlannerListAPIView, UserPlannerIDListAPIView, UserPlannerIDDetailsAPIView,
    UerMenuListAPIView,UserMenuIDDetailsAPIView, UserProfileDetailAPIView,
    )

app_name = "App_User_Mgmt"

urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('planners/', UserPlannerListAPIView.as_view()),
    path('<int:pk>/', UserDetailsRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/profile/', UserProfileDetailAPIView.as_view()),
    path('<int:pk>/favorites/'),
    path('<int:pk>/planners/', UserPlannerIDListAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:pk>/', UserPlannerIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:pk>/menu/', UerMenuListAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/<int:pk>/', UserMenuIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/sprmkt_list/', SprMktListAPIView.as_view()),
]


