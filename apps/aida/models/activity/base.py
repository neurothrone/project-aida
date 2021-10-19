from django.db import models

from shared.models.base import BaseModel


class Activity(BaseModel):
    engaged_at = models.DateTimeField(
        help_text="Enter the date and time that you engaged in the activity")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        pass
