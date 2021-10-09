from django.db import models

from .base import Set

TIME_UNITS = [
    ("min", "Minutes"),
    ("sec", "Seconds"),
    ("hour", "Hours"),
]


class CardioSet(Set):
    speed = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)
    time_unit = models.CharField(choices=TIME_UNITS, max_length=10, blank=True, null=True)
