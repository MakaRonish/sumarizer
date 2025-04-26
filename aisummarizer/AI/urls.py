from django.contrib import admin
from django.urls import path
from .views import stream_summary

urlpatterns = [
    # path("", landingpage, name="landingpage"),
    path("", stream_summary, name="stream_summary"),
]
