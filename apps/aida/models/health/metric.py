from django.db import models

from .base import Health


class HealthMetric(Health):
    measured_at = models.DateTimeField()

    class Meta:
        abstract = True
