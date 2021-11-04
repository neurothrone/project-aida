from django.db import models

from shared.models.base import BaseModel
from shared.models.urls import ViewUrlsMixin


class Activity(BaseModel, ViewUrlsMixin):
    engaged_at = models.DateTimeField(
        help_text="Enter the date and time that you engaged in the activity")

    class Meta:
        abstract = True
