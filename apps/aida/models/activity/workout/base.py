from django.db import models

from ..base import Activity

WORKOUT_TYPES = [
    ("cardio", "Cardio Workout"),
    ("weight", "Weight Workout"),
]


class Workout(Activity):
    type = models.CharField(choices=WORKOUT_TYPES, max_length=255, blank=True, null=True)
    trained_at = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.type.title()} | {self.trained_at.date()}"

    class Meta:
        ordering = ("-trained_at",)
