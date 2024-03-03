from django.conf import settings
from opensearchpy import OpenSearch

from ..exceptions import ConfigurationError
from .fields import BaseField
from .managers import OsManager
from .model_registry import registry


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
        fields = {}
        for obj_name, obj in attrs.items():
            if issubclass(obj, BaseField):
                fields[obj_name] = obj
        new_class._fields = fields
        registry.register(new_class)
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
    def render_settings(self):
        """
        This will be used to render the settings for the index
        """
        return {"index": {}}

    @classmethod
    def render_mappings(cls):
        """
        This will be used to render the mappings for the index
        """
        mappings = {}
        for name, field in cls._fields.items():
            options = {"type": field.field_type}
            # TODO: need to handle nested fields
            if field.ignore_malformed:
                options["ignore_malformed"] = field.ignore_malformed
            mappings[name] = options
        return {"properties": mappings}

    @classmethod
    def render_aliases(cls):
        """
        This will be used to render the aliases for the index
        """
        return {}

    @classmethod
    def create_index_mapping(cls):
        """
        Eventually it would be nice to handle this the same way
        django handles migrations. But will use this in the meantime
        as POC
        """
        client = OpenSearch(settings.OPENSEARCH_HOSTS)
        body = {
            "mappings": cls.render_mappings(),
            "settings": cls.render_settings(),
            "aliases": cls.render_aliases(),
        }
        client.indices.create(index=cls._meta.index_pattern, body=body)
