from django.db import models

from .base import Health


class HealthMetric(Health):
    measured_at = models.DateTimeField(help_text="Enter the date and time the measurement took place")

    class Meta:
        abstract = True
