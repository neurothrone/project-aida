from django.db import models

from aida.models.activity.exercise import Exercise
from shared.models.base import BaseModel
from shared.models.urls import ViewUrlsMixin


class Set(BaseModel, ViewUrlsMixin):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE,
                                 help_text="The exercise the set belongs to")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.exercise.name

