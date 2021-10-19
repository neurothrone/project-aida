from django.db import models

from apps.aida.models.health.base import Health
from shared.models.urls import ViewUrlsMixin


class Sleep(Health, ViewUrlsMixin):
    slept_at = models.DateTimeField(help_text="Enter the date and time you went to sleep")
    awoke_at = models.DateTimeField(help_text="Enter the date and time you woke up at")
    duration = models.PositiveIntegerField(default=0, help_text="Duration of sleep")

    class Meta:
        verbose_name_plural = "Sleep metrics"
        ordering = ["-slept_at", ]

    def __str__(self) -> str:
        return f"From {self.slept_at.date()} to {self.awoke_at.date()}"

    def save(self, *args, **kwargs):
        self.duration = int((self.awoke_at - self.slept_at).total_seconds())
        super().save(*args, **kwargs)

    def duration_formatted(self):
        total_minutes = self.duration / 60
        minutes = total_minutes % 60
        hours = (total_minutes - minutes) / 60
        return f"{hours:.0f} h {minutes:.0f} min"

    @property
    def detail_url(self) -> str:
        return "aida:sleep-detail"

    @property
    def update_url(self) -> str:
        return "aida:sleep-update"

    @property
    def delete_url(self) -> str:
        return "aida:sleep-delete"
