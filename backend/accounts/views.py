from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "accounts/register.html", {
                "error": "Passwords do not match."
            })

        if User.objects.filter(username=username).exists():
            return render(request, "accounts/register.html", {
                "error": "Username already exists."
            })

        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {
                "error": "Email already exists."
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("home")