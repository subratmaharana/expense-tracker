from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import Category , Transaction ,MonthlyIncome


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

@login_required
def expense_history(request):

    expenses = Transaction.objects.filter(
        user=request.user
    ).order_by("-date")

    return render(
        request,
        "expenses/expense_history.html",
        {
            "expenses": expenses
        }
    )

@login_required
def edit_expense(request, id):

    expense = Transaction.objects.get(
        id=id,
        user=request.user
    )

    categories = Category.objects.all()

    if request.method == "POST":

        expense.title = request.POST.get("title")
        expense.amount = request.POST.get("amount")
        expense.transaction_type = request.POST.get("transaction_type")
        expense.category = Category.objects.get(
            id=request.POST.get("category")
        )
        expense.date = request.POST.get("date")
        expense.description = request.POST.get("description")

        expense.save()

        return redirect("expense_history")

    return render(request, "expenses/edit_expense.html", {
        "expense": expense,
        "categories": categories
    })


@login_required
def delete_expense(request, id):

    expense = Transaction.objects.get(
        id=id,
        user=request.user
    )

    expense.delete()

    return redirect("expense_history")

@login_required
def set_income(request):

    income = MonthlyIncome.objects.filter(user=request.user).first()

    if request.method == "POST":

        amount = request.POST.get("amount")

        if income:
            income.amount = amount
            income.save()
        else:
            MonthlyIncome.objects.create(
                user=request.user,
                amount=amount
            )

        return redirect("dashboard")

    return render(request, "expenses/set_income.html", {
        "income": income
    })