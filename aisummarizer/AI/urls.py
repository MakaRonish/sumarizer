from django.contrib import admin
from django.urls import path
from .views import landingpage, history

urlpatterns = [
    path("", landingpage, name="landingpage"),
    path("book/<str:pk>/", history, name="book"),
    # path("", stream_summary, name="stream_summary"),
]
