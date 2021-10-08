from django.db import models

from .workout import Workout


class WeightTraining(Workout):
    type = models.CharField(default="weight_training", editable=False, max_length=25)

    class Meta:
        verbose_name_plural = "Weight workouts"

    def __str__(self) -> str:
        return "Weight Training"
