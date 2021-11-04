from django.db import models

from aida.models.interest.base import Interest


class Book(Interest):
    title = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    genre = models.CharField()
    published_at = models.DateField()

