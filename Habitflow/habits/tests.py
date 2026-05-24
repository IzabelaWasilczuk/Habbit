from datetime import date

from django.test import TestCase
from django.urls import reverse

from .models import Habit, HabitLog


class HabitModelTests(TestCase):

    def test_create_habit(self) -> None:

        habit = Habit.objects.create(name="Test", description="Opis")
        self.assertEqual(habit.name, "Test")

    def test_habit_log_unique_per_day(self) -> None:

        habit = Habit.objects.create(name="Test", description="")
        HabitLog.objects.create(habit=habit, date=date.today(), is_done=True)
        with self.assertRaises(Exception):
            HabitLog.objects.create(habit=habit, date=date.today(), is_done=False)


class HabitViewsTests(TestCase):


    def setUp(self) -> None:

        self.habit = Habit.objects.create(name="Test", description="Opis")

    def test_habit_list_view_status_code(self) -> None:

        response = self.client.get(reverse("habit_list"))
        self.assertEqual(response.status_code, 200)

    def test_habit_create_view_creates_habit(self) -> None:

        response = self.client.post(
            reverse("habit_create"),
            {"name": "Nowy", "description": "Nowy opis"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Habit.objects.filter(name="Nowy").exists())

    def test_toggle_habit_today_creates_log(self) -> None:

        self.client.post(reverse("toggle_habit_today", args=[self.habit.id]))
        self.assertTrue(
            HabitLog.objects.filter(habit=self.habit, date=date.today()).exists()
        )
