from django.contrib import admin
from django.urls import path
from .views import landingpage, history, delete_book

urlpatterns = [
    path("", landingpage, name="landingpage"),
    path("book/<str:pk>/", history, name="book"),
    path("delete/<str:pk>/", delete_book, name="delete"),
    # path("", stream_summary, name="stream_summary"),
]
