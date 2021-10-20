from django.db import models

from shared.models.base import BaseModel


class Health(BaseModel):
    class Meta:
        abstract = True

    def __str__(self) -> str:
        pass


class HealthMetric(Health):
    measured_at = models.DateTimeField(help_text="Enter the date and time the measurement took place")

    class Meta:
        abstract = True
