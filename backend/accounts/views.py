from django.shortcuts import render

# Create your views here.
def register(request):

    return render(request, "accounts/register.html")


def login_user(request):

    return render(request, "accounts/login.html")


def logout_user(request):

    pass