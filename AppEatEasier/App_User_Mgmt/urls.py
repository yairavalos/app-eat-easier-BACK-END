# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import UserAPIView, UserListAPIView

app_name = "App_User_Mgmt"

urlpatterns = [
    path('', UserAPIView.as_view()),
]

