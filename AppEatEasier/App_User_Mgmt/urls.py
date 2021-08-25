# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import (
    UserAPIView, UserListAPIView, UserDetailsRetrieveUpdateAPIView, 
    UserPlannerListAPIView, UserPlannerIDListAPIView
    )

app_name = "App_User_Mgmt"

urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('planners/', UserPlannerListAPIView.as_view()),
    path('<int:pk>/', UserDetailsRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/planners/', UserPlannerIDListAPIView.as_view()),
]


