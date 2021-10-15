from django.db import models

from shared.models.base import BaseModel


class Person(BaseModel):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
