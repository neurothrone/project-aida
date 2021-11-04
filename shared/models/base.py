from abc import abstractmethod
from datetime import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    class Meta:
        abstract = True

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError()

    def save(self, *args, **kwargs):
        """The field created_at is set only once and updated_at each time the object is modified."""
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def find_by_id(cls, id_: int):
        return cls.objects.filter(id=id_).first()

    @classmethod
    def find_all(cls):
        return cls.objects.all()

    @classmethod
    def datetime_table_format(cls, dt: datetime):
        return datetime.strftime(cls.to_local_time(dt), "%b. %d %Y, %H:%M")

    @classmethod
    def date_table_format(cls, dt: datetime):
        return datetime.strftime(cls.to_local_time(dt), "%b. %d %Y")

    @classmethod
    def to_local_time(cls, dt: datetime):
        aware_dt = make_aware(datetime.strptime(datetime.strftime(dt, "%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M"))
        time_difference = dt - aware_dt
        return dt + time_difference
