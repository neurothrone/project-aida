from django.db import models

from .base import Exercise
from ..weight import WeightTraining


class WeightExercise(Exercise):
    training = models.ForeignKey(WeightTraining, on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(default="weight_exercise", editable=False, max_length=25)

    def __str__(self) -> str:
        return self.name

    def reps(self) -> int:
        # return the total count of all reps in all sets
        pass
