from django.db import models

from apps.aida.models.training.exercise import Exercise


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise.name

    class Meta:
        abstract = True

    # TODO: abstract methods
    # to_json()
    # from_json()
