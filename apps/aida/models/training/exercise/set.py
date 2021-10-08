from django.db import models

from .base import Exercise


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="sets", on_delete=models.CASCADE)
    reps = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return self.exercise.name
