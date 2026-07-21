from django.shortcuts import render , redirect
from django.db.models import Sum ,Count
from django.db.models.functions import TruncMonth
from .forms import IncomeSourceForm
from django.contrib.auth.decorators import login_required
from .models import Category , Transaction ,IncomeSource


def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):

    total_income = IncomeSource.objects.filter(
        user=request.user
    ).aggregate(total=Sum("amount"))["total"] or 0

    total_expense = Transaction.objects.filter(
        user=request.user,
        transaction_type="Expense"
    ).aggregate(total=Sum("amount"))["total"] or 0

    remaining_balance = total_income - total_expense

    total_transactions = Transaction.objects.filter(
        user=request.user
    ).count()

    recent_transactions = Transaction.objects.filter(
        user=request.user
    ).order_by("-date")[:5]

    category_expenses = (
        Transaction.objects.filter(
            user=request.user,
            transaction_type="Expense"
        )
        .values("category__name")
        .annotate(total=Sum("amount"))
    )

    monthly_expenses=(
    Transaction.objects.filter(
        user=request.user,
        transaction_type="Expense"
    )
    .annotate(month=TruncMonth("date"))
    .values("month")
    .annotate(total=Sum("amount"))
    .order_by("month")
    )
    monthly_income=(
    IncomeSource.objects.filter(
        user=request.user
    )
    .annotate(month=TruncMonth("date"))
    .values("month")
    .annotate(total=Sum("amount"))
    .order_by("month")
)

    line_labels=[]
    income_data=[]
    expense_data=[]

    income_dict={}
    expense_dict={}

    for item in monthly_income:
        income_dict[item["month"].strftime("%b")]=float(item["total"])

    for item in monthly_expenses:   
        expense_dict[item["month"].strftime("%b")]=float(item["total"])

    months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

    for month in months:
        if month in income_dict or month in expense_dict:
            line_labels.append(month)
            income_data.append(income_dict.get(month,0))
            expense_data.append(expense_dict.get(month,0))

    bar_labels=[]
    bar_data=[]

    for item in monthly_expenses:
        bar_labels.append(item["month"].strftime("%b"))
        bar_data.append(float(item["total"]))

    chart_labels = []
    chart_data = []

    for item in category_expenses:
        chart_labels.append(item["category__name"])
        chart_data.append(float(item["total"]))

    context = {
        "total_income": total_income,
        "total_expense": total_expense,
        "remaining_balance": remaining_balance,
        "total_transactions": total_transactions,
        "recent_transactions": recent_transactions,
        "chart_labels": chart_labels,
        "chart_data": chart_data,
        "bar_labels":bar_labels,
        "bar_data":bar_data,
        "line_labels":line_labels,
        "income_data":income_data,
        "expense_data":expense_data,
    }

    return render(request, "expenses/dashboard.html", context)


@login_required
def view_category(request):
    categories = Category.objects.all()

    return render(request, "expenses/view_categories.html", {
        "categories": categories
    })


@login_required
def add_expense(request):

    categories = Category.objects.all()
    income_sources = IncomeSource.objects.filter(user=request.user)

    if request.method == "POST":

        Transaction.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            amount=request.POST.get("amount"),
            transaction_type="Expense",
            category=Category.objects.get(id=request.POST.get("category")),
            paid_from=IncomeSource.objects.get(id=request.POST.get("paid_from")),
            date=request.POST.get("date"),
            description=request.POST.get("description"),
        )

        return redirect("expense_history")

    return render(request, "expenses/add_expense.html", {
        "categories": categories,
        "income_sources": income_sources,
    })

@login_required
def expense_history(request):

    expenses = Transaction.objects.filter(
        user=request.user ,
        transaction_type="Expense"
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
def income_list(request):

    incomes = IncomeSource.objects.filter(user=request.user)

    total_income = sum(income.amount for income in incomes)

    return render(request, "expenses/income_list.html", {
        "incomes": incomes,
        "total_income": total_income,
    })

@login_required
def add_income(request):

    if request.method == "POST":

        form = IncomeSourceForm(request.POST)

        if form.is_valid():

            income = form.save(commit=False)
            income.user = request.user
            income.save()

            return redirect("income_list")

    else:

        form = IncomeSourceForm()

    return render(request, "expenses/add_income.html", {
        "form": form
    })