# Standard Libraries and Packages:

from rest_framework import status
from rest_framework import generics, serializers, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django_filters.rest_framework import DjangoFilterBackend

# Serializers:
from .serializers import (
    UserRecipeDetailSerializer, UserSerializer, UserDetailSerializer, UserListSerializer, UserMenuListSerializer, 
    UserPlannerListSerializer, UserPlannerDetailSerializer, UserPlannerCreateDetailSerializer, UserMenuDetailSerializer, 
    UserProfileSerializer, UserProfileAppSerializer, UserProfileEditAppsSerializer, UserProfileFoodSerializer, 
    UserProfileRecipeSerializer, UserFavoritesListSerializer, UserFavoritesListCreateSerializer, UserProfilePeopleQtySerializer,
    UserProfileEditFoodSerializer, UserRecipeListSerializer, UserMenuDetailCreateSerializer # -> to be reviewed
)

from App_Recipe_Mgmt.serializers import UserSuggestionListSerializer


# Models:
from .models import User, UserProfile, UserApp, UserFood, UserRecipe, UserMenu, UserPlanner
from App_Recipe_Mgmt.models import CatalogRecipe, RecipeApp, RecipeIngredient

# Create your views here.

# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER CREATION AND MANAGEMENT
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserAPIView(APIView):
    """
    This view its the first view from template for testing purposes
    """
    def get(self, request):
        return Response("This User Main Page View")


class UserCreateAPIView(generics.CreateAPIView):
    """
    This view its intended for User  Generation
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        user = User.objects.get(id=token.user_id)
        return Response({'id':token.user_id, 'username':user.username, 'token': token.key })


class UserIDAuthTokenView(ObtainAuthToken):
    """
    This view its intended to give a little more detail in order to 
    address users correctly into end-points filters
    """

    def post(self, request, *args, **kwargs):
        response =  super(UserIDAuthTokenView, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({'id':token.user_id, 'user':user.username, 'token': token.key })


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



# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER PREFERENCES PROFILE CREATION AND MANAGEMENT
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserProfileQtyView(generics.ListCreateAPIView): # To POST just change to ListCreateAPIView
    """
    This view its purpose its to handle Qty Preferences from User Profile
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfilePeopleQtySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']
    
    
class UserProfileAppsView(generics.ListCreateAPIView): # To POST Kitchen Appliances
    """
    This view its purpose its to handle User´s Food Preferences
    """

    queryset = UserApp.objects.all()
    serializer_class = UserProfileEditAppsSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']

    def post(self, request):
        data = request.data
        
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileFoodView(generics.ListCreateAPIView): # To POST Food Preferences
    """
    This view its purpose its to handle User´s Food Preferences
    """

    queryset = UserFood.objects.all()
    serializer_class = UserProfileEditFoodSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']
    
    def post(self, request):
        data = request.data
        
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER PROFILED RECOMMENDATIONS / AUTOMATIC PROCESSING
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserProfiledRecommendationsList(generics.ListAPIView):
    """
    This view its purpose its to provide an automatic list of suggestions based on user profile preferences
    """
    
    queryset = UserRecipe.objects.all() # -> In the meanwhile, its just fine
    serializer_class = UserSuggestionListSerializer # -> Its NOT well Defined, need to be reviewed
    

    def get_queryset_recipe_foods(self):

        user_id = self.kwargs['pk']
        filter = {}

        if user_id:
            filter['user_profile_id'] = user_id

        # user_foods = UserFood.objects.filter(**filter)
        food_list = UserFood.objects.filter(**filter) #-> According to tests results
        recipes = CatalogRecipe.objects.filter(food_type__in=food_list.values('food_type')) #-> According to tests results
        recipes_id = [item['id'] for item in recipes.values('id')] #-> According to tests results
        return recipes


    def list(self, request, *args, **kwargs):
        user_profile_recipes = UserSuggestionListSerializer(self.get_queryset_recipe_foods(), many=True)

        return Response(user_profile_recipes.data)


class UserProfileFavoriteListCreate(generics.ListCreateAPIView):
    """
    This view its purpose its to Save Suggested Recipes into User Favorites Table
    """
    pass

    queryset = UserRecipe.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']
    
    def get_serializer_class(self):

        if self.request.method == 'GET':
            serializer_class = UserFavoritesListSerializer
        
        if self.request.method == 'POST':
            serializer_class = UserFavoritesListCreateSerializer
        return serializer_class

    def post(self, request):
        data = request.data

        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER PLANNERS AND MENU GENERATION INCLUDING MANAGEMENT
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserPlannerListAPIView(generics.ListAPIView): # To POST just change to ListCreateAPIView
    """
    This view its purpose its to list total User´s Planner
    """

    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerListSerializer


class UserPlannerListCreateView(generics.ListCreateAPIView): # To POST New Menu´s Planners
    """
    This view its purpose its to handle User´s New Menu Planner Generation
    """

    queryset = UserPlanner.objects.all()
    serializer_class = UserPlannerCreateDetailSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']
    

    def post(self, request):
        data = request.data
        
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMenuListCreateView(generics.ListCreateAPIView):
    """
    This view its purpose its to handle User´s Menú Planner Recipes by day and time 

    This is a just one step before to create The Super Market List
    """

    queryset = UserMenu.objects.all()
    serializer_class = UserMenuDetailCreateSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=user_profile__id']
    ordering_fields = ['user_profile']

    def post(self, request):
        data = request.data
        
        if isinstance(data, list):
            serializer = self.get_serializer(data=data, many=True)
        else:
            serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ------------------------------------------------------------------------------------------------------------------------------------
#
# USER EXTRAS FOR MANUAL SEARCHING AND VALIDATIONS
#
# ------------------------------------------------------------------------------------------------------------------------------------


class UserFavoriteIDListAPIView(generics.ListAPIView): # To POST just change to ListCreateAPIView
    """
    This view its purpose is to list total User´s Favorites from Recipe´s Catalog
    """

    serializer_class = UserFavoritesListSerializer

    def get_queryset(self):

        user_profile_id = self.kwargs['pk']
        filter = {}

        if user_profile_id:
            filter['user_profile_id'] = user_profile_id
            filter['favorite'] = True

        return UserRecipe.objects.filter(**filter)



class UserProfileDetailAPIView(generics.ListAPIView):
    """
    This view its purpose its to retrieve full user profile including preferences
    """
    
    def get_queryset(self):

        user_id = self.kwargs['pk']
        filter = {}

        if user_id:
            filter['user_profile_id'] = user_id

        return UserProfile.objects.filter(**filter)

    def get_queryset_apps(self):

        user_id = self.kwargs['pk']
        filter = {}

        if user_id:
            filter['user_profile_id'] = user_id

        return UserApp.objects.filter(**filter)

    def get_queryset_foods(self):

        user_id = self.kwargs['pk']
        filter = {}

        if user_id:
            filter['user_profile_id'] = user_id

        return UserFood.objects.filter(**filter)

    def get_queryset_recipes(self):

        user_id = self.kwargs['pk']
        filter = {}

        if user_id:
            filter['user_profile_id'] = user_id

        return UserRecipe.objects.filter(**filter)

    def list(self, request, *args, **kwargs):
        user_profile = UserProfileSerializer(self.get_queryset(), many=True)
        user_profile_apps = UserProfileAppSerializer(self.get_queryset_apps(), many=True)
        user_profile_foods = UserProfileFoodSerializer(self.get_queryset_foods(), many=True)
        user_profile_recipes = UserProfileRecipeSerializer(self.get_queryset_recipes(), many=True)

        return Response(
            {
            "user_profile": user_profile.data,
            "user_profile_apps": user_profile_apps.data,
            "user_profile_foods": user_profile_foods.data,
            "user_profile_recipes": user_profile_recipes.data
            }
        )


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


class UserMenuListAPIView(generics.ListAPIView): # To POST just change to ListCreateAPIView
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

