from .models import Category
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request) :
    return render (request , "home.html") 

@login_required
def dashboard(request):
    return render(request, "expenses/dashboard.html")

@login_required
def category_list(request):
    categories = Category.objects.filter(user=request.user)
    return render(request, "expenses/category_list.html", {
        "categories": categories
    })

@login_required
def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")

        Category.objects.create(
            user=request.user,
            name=name
        )

        return redirect("category_list")

    return render(request, "expenses/add_category.html")