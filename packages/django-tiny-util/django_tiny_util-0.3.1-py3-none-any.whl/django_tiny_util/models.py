"""
Copyright (c) 2020 Oleg Bogumirski <reg@olegb.ru>
"""
from typing import Optional

from django.db.models import Model


def get_or_none(cls: type(Model), **kwargs) -> Optional[Model]:
    try:
        return cls.objects.get(**kwargs)
    except cls.DoesNotExist:
        return None


def update_fields(model: Model, **kwargs):
    fields = list(kwargs.keys())

    for key in fields:
        setattr(model, key, kwargs[key])

    model.save(update_fields=fields)


def get_or_create_or_update(cls: type(Model), unique_fields: dict, default_or_update_fields: dict) -> (Model, bool):
    res, created = cls.objects.get_or_create(**unique_fields, defaults=default_or_update_fields)
    if not created:
        update_fields(res, **default_or_update_fields)

    return res, created
