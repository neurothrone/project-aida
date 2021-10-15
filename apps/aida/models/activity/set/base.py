from django.db import models

from shared.models.base import BaseModel
from apps.aida.models.activity.exercise import Exercise


# TODO: inherit BaseModel
class Set(BaseModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.exercise.name

    class Meta:
        abstract = True

