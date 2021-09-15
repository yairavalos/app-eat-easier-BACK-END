# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as authtoken_views

# External Views
from App_SprMkt_Mgmt.views import SprMktListAPIView

# Views:
from .views import (
    UserAPIView, UserIDAuthTokenView, UserListAPIView, UserDetailsRetrieveUpdateAPIView, 
    UserProfileQtyView, UserProfileAppsView, UserProfileFoodView, 
    UserProfiledRecommendationsList, UserProfileFavoriteListCreate,
    UserPlannerListCreateView,
    UserFavoriteIDListAPIView, UserPlannerIDListAPIView, UserPlannerIDDetailsAPIView,
    UserMenuListAPIView, UserMenuListCreateView, UserShoppingListView,
    UserMenuIDDetailsAPIView, UserProfileDetailAPIView, UserCreateAPIView
    )

app_name = "App_User_Mgmt"

urlpatterns = [
    # Initial Template
    path('', UserListAPIView.as_view()),
    # User Registration
    path('signup/', UserCreateAPIView.as_view(), name="sign-up"),
    path('login/', UserIDAuthTokenView.as_view(), name='token_login'),
    # Listing, searching and Posting
    path('profiles/qty/', UserProfileQtyView.as_view()), # POST -> User Profile People Amount
    path('profiles/apps/', UserProfileAppsView.as_view()), # POST -> User Profile Food Preferences
    path('profiles/food/', UserProfileFoodView.as_view()), # POST -> User Profile Food Preferences
    path('profiles/suggest/<int:pk>/', UserProfiledRecommendationsList.as_view()), # GET -> Automatic List of Suggestions
    path('profiles/favorite/', UserProfileFavoriteListCreate.as_view()), # GET / POST -> User Favorites Recipes Creation
    path('profiles/planner/', UserPlannerListCreateView.as_view()), # POST -> User New Menu Creation
    path('profiles/planner/menu/', UserMenuListCreateView.as_view(),), # POST ----> SAVE User Menu <--------- More validation !!!!!!!
    path('profiles/shopping_list/<int:pk>/', UserShoppingListView.as_view()),
    # Just for validate specific user views data
    path('<int:pk>/', UserDetailsRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/favorites/', UserFavoriteIDListAPIView.as_view()),
    path('<int:pk>/planners/', UserPlannerIDListAPIView.as_view()), 
    path('<int:pk>/profile/', UserProfileDetailAPIView.as_view()), 
    path('<int:user_profile_id>/planners/<int:pk>/', UserPlannerIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:pk>/menu/', UserMenuListAPIView.as_view()), # --> GET -> Menu Viewer -> Display
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/<int:pk>/', UserMenuIDDetailsAPIView.as_view()),
    path('<int:user_profile_id>/planners/<int:user_planner_id>/menu/sprmkt_list/', SprMktListAPIView.as_view()),
]


