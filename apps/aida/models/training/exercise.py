from django.db import models

from apps.aida.models.training.workout import Workout


EXERCISE_TYPES = [
    ("cardio", "Cardio"),
    ("weight", "Weight"),
    ("undefined", "Undefined"),
]


class Exercise(models.Model):
    training = models.ForeignKey(Workout, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(choices=EXERCISE_TYPES, max_length=25, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    vest_weight = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.name
