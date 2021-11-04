from abc import abstractmethod

from django.db import models


class DataConvertableMixin(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def _delete_data_from_db(cls) -> None:
        cls.objects.all().delete()

    @classmethod
    def populate_db_from_csv(cls, data: list[list[str]]) -> None:
        cls._delete_data_from_db()
        for datum in data:
            cls.create(*datum)

    @classmethod
    def populate_db_from_json(cls, data: list[dict]) -> None:
        cls._delete_data_from_db()
        for datum in data:
            cls.create(**datum)

    @staticmethod
    @abstractmethod
    def create(*args, **kwargs):
        pass

    @staticmethod
    @abstractmethod
    def db_data_to_csv():
        pass

    @staticmethod
    @abstractmethod
    def db_data_to_json():
        pass
