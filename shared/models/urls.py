from abc import abstractmethod

from django.db import models
from django.urls import reverse


class ViewUrlsMixin(models.Model):
    class Meta:
        abstract = True

    @property
    @abstractmethod
    def create_url(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def detail_url(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def update_url(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def delete_url(self) -> str:
        raise NotImplementedError()

    def get_create_url(self):
        """Returns the url to create a record for this object."""
        return reverse(self.create_url, args=[str(self.id)])

    def get_absolute_url(self):
        """Returns the url to access a detail record for this object."""
        return reverse(self.detail_url, args=[str(self.id)])

    def get_update_url(self):
        """Returns the url to update a record for this object."""
        return reverse(self.update_url, args=[str(self.id)])

    def get_delete_url(self):
        """Returns the url to delete a record for this object."""
        return reverse(self.delete_url, args=[str(self.id)])
