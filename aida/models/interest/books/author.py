from django.db import models

from .book import Book
from ..person import Person


class Author(Person):
    books = models.ManyToManyField(Book, related_name="authors")
