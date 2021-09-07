# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

# External Views
from App_SprMkt_Mgmt.views import SprMktListAPIView

# Views:
from .views import (
    UserAPIView, UserIDAuthTokenView, UserListAPIView, UserDetailsRetrieveUpdateAPIView, 
    UserProfileQtyView, UserProfileQtyEditView,
    UserPlannerListAPIView, UserPlannerIDListAPIView, UserPlannerIDDetailsAPIView,
    UerMenuListAPIView,UserMenuIDDetailsAPIView, UserProfileDetailAPIView, UserFavoriteListAPIView, UserCreateAPIView
    )

app_name = "App_User_Mgmt"

urlpatterns = [
    path('', UserListAPIView.as_view()),
    path('signup/', UserCreateAPIView.as_view(), name="sign-up"),
    path('login/', UserIDAuthTokenView.as_view(), name='token_login'),
    path('planners/', UserPlannerListAPIView.as_view()),
    path('profiles/qty/', UserProfileQtyView.as_view()), # POST -> User
    path('<int:pk>/', UserDetailsRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/favorites/', UserFavoriteListAPIView.as_view()),
    path('<int:pk>/planners/', UserPlannerIDListAPIView.as_view()),
    path('<int:pk>/profile/', UserProfileDetailAPIView.as_view()),
    path('<int:pk>/profile/qty/edit/', UserProfileQtyEditView.as_view()),
    path('<int:user_profile_id>/planners/<int:pk>/', UserPlannerIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:pk>/menu/', UerMenuListAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/<int:pk>/', UserMenuIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/sprmkt_list/', SprMktListAPIView.as_view()),
]


