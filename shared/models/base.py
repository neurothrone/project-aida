import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def find_by_id(cls, _id):
        return cls.objects.filter(id=_id).first()

    class Meta:
        abstract = True
