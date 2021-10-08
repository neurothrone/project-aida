from django.db import models

from .base import Exercise


class CardioExercise(Exercise):
    type = models.CharField(default="cardio_exercise", editable=False, max_length=25)

