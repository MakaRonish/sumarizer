from django.contrib import admin
from django.urls import path
from .views import landingpage

urlpatterns = [
    path("", landingpage, name="landingpage"),
]
