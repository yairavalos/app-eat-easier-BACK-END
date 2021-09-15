# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import SprMktAPIView

app_name = "App_SprMkt_Mgmt"

urlpatterns = [
    path('', SprMktAPIView.as_view()),
]
