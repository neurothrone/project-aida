from django.db import models

from .base import Set


class CardioSet(Set):
    speed = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveSmallIntegerField(default=0)
