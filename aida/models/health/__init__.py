from shared.models.base import BaseModel
from shared.models.data import DataConvertableMixin
from shared.models.urls import ViewUrlsMixin


class Health(BaseModel, DataConvertableMixin, ViewUrlsMixin):
    class Meta:
        abstract = True
