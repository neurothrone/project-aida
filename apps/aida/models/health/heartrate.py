from django.db import models

from .metric import HealthMetric


class HeartRate(HealthMetric):
    pulse = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Pulse metrics"
