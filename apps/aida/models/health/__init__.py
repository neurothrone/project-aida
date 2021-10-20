from django.db import models

from shared.models.base import BaseModel
from shared.models.urls import ViewUrlsMixin


class Health(BaseModel, ViewUrlsMixin):
    class Meta:
        abstract = True


# TODO: abstract method status to be inherited by subclasses and implemented to yield
#       extra information about metrics
class HealthMetric(Health):
    measured_at = models.DateTimeField(help_text="Enter the date and time the measurement took place")

    class Meta:
        abstract = True
