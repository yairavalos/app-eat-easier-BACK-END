# Standard Libraries and Packages:

from django.contrib import admin
from django.urls import path, include

# Views:
from .views import SprMktListAPIView

app_name = "App_SprMkt_Mgmt"

urlpatterns = [
    path('', SprMktListAPIView.as_view()),
]
