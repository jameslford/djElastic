from django.conf import settings
from opensearchpy import OpenSearch

from ..exceptions import ConfigurationError
from .managers import OsManager


class OsModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        attr_meta = attrs.pop("Meta", None)
        abstract = getattr(attr_meta, "abstract", False)
        meta = attr_meta or getattr(new_class, "Meta", None)
        if not meta:
            raise ConfigurationError(
                f"{new_class.__name__} must define a Meta class with\
                      either `abstract = True` or `index_pattern` attribute."
            )
        if not abstract:
            if not hasattr(meta, "index_pattern"):
                raise ConfigurationError(
                    f"{new_class.__name__} must define a Meta class\
                          with `index pattern` attribute."
                )
        setattr(new_class, "_meta", meta)
        return new_class

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        required_attrs = ["index_pattern"]
        for attr in required_attrs:
            if attr not in attrs:
                raise ValueError(f"OsModel must define {attr}")

    @property
    def objects(cls) -> OsManager:
        if not hasattr(cls, "_objects"):
            cls._objects = OsManager(cls)
        return cls._objects


class OsModel(metaclass=OsModelBase):
    """
    Nesting fields will be supported with dot notation
    """

    def save(self):
        pass

    @classmethod
    def render_mappings(cls):
        """
        This will be used to render the mappings for the index
        """
        pass

    @classmethod
    def create_index_mapping(cls):
        """
        Eventually it would be nice to handle this the same way
        django handles migrations. But will use this in the meantime
        as POC
        """
        client = OpenSearch(settings.OPENSEARCH_HOSTS)
