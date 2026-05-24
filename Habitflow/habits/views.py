from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from .models import Habit, HabitLog
from .forms import HabitForm


def habit_list(request: HttpRequest) -> HttpResponse:

    today = date.today()
    habits = Habit.objects.all()


    for habit in habits:
        habit.today_log = HabitLog.objects.filter(habit=habit, date=today).first()

    return render(
        request,
        "habits/habit_list.html",
        {"habits": habits, "today": today},
    )


def habit_create(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("habit_list")
    else:
        form = HabitForm()

    return render(request, "habits/habit_form.html", {"form": form})


def habit_update(request: HttpRequest, habit_id: int) -> HttpResponse:

    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect("habit_list")
    else:
        form = HabitForm(instance=habit)

    return render(request, "habits/habit_form.html", {"form": form, "habit": habit})


def habit_delete(request: HttpRequest, habit_id: int) -> HttpResponse:

    habit = get_object_or_404(Habit, id=habit_id)

    if request.method == "POST":
        habit.delete()
        return redirect("habit_list")

    return render(
        request,
        "habits/habit_detail.html",
        {"habit": habit, "confirm_delete": True},
    )


def toggle_habit_today(request: HttpRequest, habit_id: int) -> HttpResponse:

    habit = get_object_or_404(Habit, id=habit_id)
    today = date.today()

    log, created = HabitLog.objects.get_or_create(habit=habit, date=today)
    log.is_done = not log.is_done
    log.save()

    return redirect("habit_list")


def habit_stats(request: HttpRequest, habit_id: int) -> HttpResponse:

    habit = get_object_or_404(Habit, id=habit_id)
    logs = habit.logs.order_by("date")

    total = logs.count()
    done = logs.filter(is_done=True).count()

    # streak
    streak = 0
    for log in reversed(list(logs)):
        if log.is_done:
            streak += 1
        else:
            break

    percent = (done / total * 100) if total > 0 else 0

    return render(
        request,
        "habits/habit_stats.html",
        {"habit": habit, "logs": logs, "streak": streak, "percent": percent},
    )
