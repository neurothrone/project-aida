from django.db.models import Model


def get_field_verbose_name(model: Model, attribute: str) -> str:
    return model._meta.get_field(attribute).verbose_name


def get_field_max_length(model: Model, attribute: str) -> int:
    return model._meta.get_field(attribute).max_length
