from django.db import models

from shared.models.base import BaseModel


class Activity(BaseModel):
    engaged_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
