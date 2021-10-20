from django.db import models

from apps.aida.models.health import HealthMetric
from shared.models.urls import ViewUrlsMixin


class HeartRate(HealthMetric, ViewUrlsMixin):
    pulse = models.PositiveSmallIntegerField(help_text="Enter your hearts beats per minute")

    class Meta:
        verbose_name_plural = "Heart rate metrics"
        ordering = ["-measured_at"]

    def __str__(self) -> str:
        return f"{self.measured_at.date()} | {self.pulse}"

    @property
    def detail_url(self) -> str:
        return "aida:hr-detail"

    @property
    def update_url(self) -> str:
        return "aida:hr-update"

    @property
    def delete_url(self) -> str:
        return "aida:hr-delete"
