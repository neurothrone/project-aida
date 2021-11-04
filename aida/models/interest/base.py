from django.db import models

from shared.models.base import BaseModel


class Interest(BaseModel):
    finished_at = models.DateTimeField()

    class Meta:
        abstract = True
