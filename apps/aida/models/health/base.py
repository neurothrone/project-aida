from shared.models.base import BaseModel


class Health(BaseModel):
    class Meta:
        abstract = True

    def __str__(self) -> str:
        pass
