from django.db import models

from apps.aida.models.health import HealthMetric
from shared.models.urls import ViewUrlsMixin


class BloodPressure(HealthMetric, ViewUrlsMixin):
    systolic = models.PositiveSmallIntegerField(help_text="Enter the systolic value (the upper value)")
    diastolic = models.PositiveSmallIntegerField(help_text="Enter diastolic value (the lower value)")

    class Meta:
        verbose_name_plural = "Blood pressure metrics"
        ordering = ["-measured_at"]

    def __str__(self) -> str:
        return f"{self.measured_at.date()} | {self.systolic / self.diastolic}"

    @property
    def detail_url(self) -> str:
        return "aida:bp-detail"

    @property
    def update_url(self) -> str:
        return "aida:bp-update"

    @property
    def delete_url(self) -> str:
        return "aida:bp-delete"
