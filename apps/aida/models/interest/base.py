from django.db import models

from shared.models.base import BaseModel


class Interest(BaseModel):
    class Meta:
        abstract = True
