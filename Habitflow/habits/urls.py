from django.urls import path
from . import views

urlpatterns = [
    path("", views.habit_list, name="habit_list"),
    path("habit/add/", views.habit_create, name="habit_create"),
    path("habit/<int:habit_id>/edit/", views.habit_update, name="habit_update"),
    path("habit/<int:habit_id>/delete/", views.habit_delete, name="habit_delete"),
    path("habit/<int:habit_id>/toggle/", views.toggle_habit_today, name="toggle_habit_today"),
    path("habit/<int:habit_id>/stats/", views.habit_stats, name="habit_stats"),
]
