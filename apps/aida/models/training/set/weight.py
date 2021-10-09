from django.db import models

from .base import Set

WEIGHT_UNITS = [
    ("g", "Grams"),
    ("kg", "Kilograms"),
    ("lb", "Pounds"),
]


class WeightSet(Set):
    reps = models.PositiveSmallIntegerField(default=0)
    weight = models.PositiveSmallIntegerField(default=0)
    weight_unit = models.CharField(choices=WEIGHT_UNITS, max_length=10, blank=True, null=True)

