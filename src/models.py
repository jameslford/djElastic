from typing import Type

from elasticsearch_dsl import Document, Field

from .managers import BaseEsManager


class EsModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = None
        return new_class

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        required_attrs = ["index_pattern"]
        print(f"attrs: {attrs}")
        for attr in required_attrs:
            if attr not in attrs:
                raise ValueError(f"EsModel must define {attr}")


class EsModel(Document, metaclass=EsModelBase):

    objects = BaseEsManager()

    @classmethod
    def get_field_type(cls, field_name) -> Type[Field]:
        return cls._doc_type.mapping[field_name]["type"]
