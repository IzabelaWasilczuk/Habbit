from django.db import models


class Habit(models.Model):

    name = models.CharField(max_length=100, default="Unnamed habit")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:

        return self.name


class HabitLog(models.Model):

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="logs")
    date = models.DateField()
    is_done = models.BooleanField(default=False)

    class Meta:
        unique_together = ("habit", "date")

    def __str__(self) -> str:

        status = "done" if self.is_done else "not done"
        return f"{self.habit.name} on {self.date} ({status})"
