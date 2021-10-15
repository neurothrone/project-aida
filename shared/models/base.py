# import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    # uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Set created_at only once and updated_at each time object is modified."""
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
