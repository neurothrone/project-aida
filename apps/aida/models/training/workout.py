from django.db import models

WORKOUT_TYPES = [
    ("cardio", "Cardio Workout"),
    ("weight", "Weight Workout"),
]


class Workout(models.Model):
    name = models.CharField(choices=WORKOUT_TYPES, max_length=255, blank=True, null=True)
    trained = models.DateTimeField(blank=True, null=True)

    # def __str__(self) -> str:
    #     return self.name
