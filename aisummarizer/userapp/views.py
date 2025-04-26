from django.shortcuts import render
from .form import CustomUserForm

# Create your views here.


def loginIn(request):
    return render(request, "userapp/login.html")


def signup(request):
    form = CustomUserForm()
    context = {"form": form}
    return render(request, "userapp/signup.html", context)
