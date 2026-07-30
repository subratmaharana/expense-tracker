from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("categories/", views.view_category, name="view_category"),
    path("expenses/add/",views.add_expense,name="add_expense"),
    path("expenses/history/", views.expense_history, name="expense_history"),
    path("expenses/edit/<int:id>/", views.edit_expense, name="edit_expense"),
    path("expenses/delete/<int:id>/", views.delete_expense, name="delete_expense"),
   
    path("income/", views.income_list, name="income_list"),
    path("income/add/", views.add_income, name="add_income"),
    path("set-budget/",views.set_budget,name="set_budget"),
    path(
    "export-pdf/",
    views.export_pdf,
    name="export_pdf",
    ),
    path(
    "export-excel/",
    views.export_excel,
    name="export_excel",
    ),
    path("reports/", views.reports, name="reports"),
    path("profile/", views.profile, name="profile"),
    path(
    "profile/edit/",
    views.edit_profile,
    name="edit_profile" ),
]