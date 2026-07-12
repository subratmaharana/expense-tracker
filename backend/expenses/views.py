from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Category


def home(request):
    return render(request, "home.html")


@login_required
def dashboard(request):
    return render(request, "expenses/dashboard.html")


@login_required
def view_category(request):
    categories = Category.objects.all()

    return render(request, "expenses/view_categories.html", {
        "categories": categories
    })