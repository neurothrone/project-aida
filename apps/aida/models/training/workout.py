from django.db import models

from shared.models.base import BaseModel

WORKOUT_TYPES = [
    ("cardio", "Cardio Workout"),
    ("weight", "Weight Workout"),
]


class Workout(BaseModel):
    type = models.CharField(choices=WORKOUT_TYPES, max_length=255, blank=True, null=True)
    trained = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.type.title()} | {self.trained.date()}"

    class Meta:
        ordering = ("-trained",)
