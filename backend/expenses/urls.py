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
]