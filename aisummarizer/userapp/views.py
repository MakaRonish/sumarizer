from django.shortcuts import render, redirect
from .form import CustomUserForm
from django.contrib.auth import authenticate

# Create your views here.


def loginIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect("signup")
        else:
            return redirect("landingpage")

    return render(request, "userapp/login.html")


def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("landingpagein")

    else:
        form = CustomUserForm()

    context = {"form": form}
    return render(request, "userapp/signup.html", context)
