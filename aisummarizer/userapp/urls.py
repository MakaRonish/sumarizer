from django.contrib import admin
from django.urls import path
from .views import loginIn, signup, logoff


urlpatterns = [
    path("logon/", loginIn, name="logon"),
    path("signup/", signup, name="signup"),
    path("logoff/", logoff, name="logoff"),
]
