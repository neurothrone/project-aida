from django.db import models

from .base import Health


class Sleep(Health):
    awake_at = models.DateTimeField()
    slept_at = models.DateTimeField()
    duration = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.duration = int((self.awake_at - self.slept_at).total_seconds())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Sleep metrics"
