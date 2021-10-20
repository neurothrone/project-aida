from django.db import models

from shared.models.base import BaseModel
from apps.aida.models.activity.exercise import Exercise


class Set(BaseModel):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE,
                                 help_text="The exercise the set belongs to")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.exercise.name

