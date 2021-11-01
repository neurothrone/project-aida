from shared.models.base import BaseModel
from shared.models.urls import ViewUrlsMixin


class Health(BaseModel, ViewUrlsMixin):
    class Meta:
        abstract = True
