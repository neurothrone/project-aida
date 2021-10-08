from django.db import models

from apps.aida.models.training.exercise import Exercise


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, related_name="sets", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise.name
