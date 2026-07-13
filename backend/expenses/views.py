from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Category , Transaction


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

@login_required
def add_expense(request):

    categories = Category.objects.all()

    if request.method == "POST":

        category = Category.objects.get(
            id=request.POST.get("category")
        )

        Transaction.objects.create(

            user=request.user,

            title=request.POST.get("title"),

            amount=request.POST.get("amount"),

            transaction_type=request.POST.get("transaction_type"),

            category=category,

            date=request.POST.get("date"),

            description=request.POST.get("description")

        )

        return redirect("dashboard")

    return render(
        request,
        "expenses/add_expense.html",
        {
            "categories": categories
        }
    )