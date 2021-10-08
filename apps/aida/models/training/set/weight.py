from django.db import models

from .base import Set


class WeightSet(Set):
    weight = models.PositiveSmallIntegerField(default=0)
    reps = models.PositiveSmallIntegerField(default=0)
