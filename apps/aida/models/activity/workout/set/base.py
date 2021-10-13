from django.db import models

from apps.aida.models.activity.workout.exercise import Exercise


# TODO: inherit BaseModel
class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise.name

    class Meta:
        abstract = True

