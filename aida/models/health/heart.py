from django.db import models

from aida.models.health import Health


class Heart(Health):
    measured_at = models.DateTimeField(help_text="Enter the date and time the measurement took place")
    systolic = models.PositiveSmallIntegerField(help_text="Enter the systolic value (the upper value)")
    diastolic = models.PositiveSmallIntegerField(help_text="Enter diastolic value (the lower value)")
    pulse = models.PositiveSmallIntegerField(help_text="Enter your hearts beats per minute")

    class Meta:
        verbose_name_plural = "Heart metrics"
        ordering = ["-measured_at"]

    def __str__(self) -> str:
        return f"{self.measured_at.date()} |{self.systolic / self.diastolic} | {self.pulse}"

    @property
    def detail_url(self) -> str:
        return "aida:heart-detail"

    @property
    def update_url(self) -> str:
        return "aida:heart-update"

    @property
    def delete_url(self) -> str:
        return "aida:heart-delete"
