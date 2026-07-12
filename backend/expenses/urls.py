from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("categories/", views.category_list, name="category_list"),
    path("categories/add/", views.add_category, name="add_category"),
]