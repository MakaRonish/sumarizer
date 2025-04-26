from django.contrib import admin
from django.urls import path
from .views import loginIn, signup


urlpatterns = [
    path("logon/", loginIn, name="logOn"),
    path("signup/", signup, name="signup"),
]
