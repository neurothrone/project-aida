from django.db import models

from .metric import HealthMetric


class BloodPressure(HealthMetric):
    systolic = models.PositiveSmallIntegerField()
    diastolic = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Blood pressure metrics"
