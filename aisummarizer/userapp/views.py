from django.shortcuts import render, redirect
from .form import CustomUserForm
from django.contrib.auth import authenticate, logout, login

# Create your views here.


def loginIn(request):
    context = {"log": True}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("landingpage")
        else:
            return redirect("signup")

    return render(request, "userapp/login.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            userinfo = form.save(commit=False)
            userinfo.save()

            login(request, userinfo)

            return redirect("landingpage")

    else:
        form = CustomUserForm()

    context = {"form": form, "log": False}
    return render(request, "userapp/signup.html", context)


def logoff(request):
    logout(request)
    return redirect("logon")
