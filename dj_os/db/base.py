from django.conf import settings
from opensearchpy import OpenSearch

from ..exceptions import ConfigurationError
from ..utils import unflatten
from .fields import BaseField
from .managers import OsManager
from .model_registry import registry
from .options import Options


class OsModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        parents = [b for b in bases if isinstance(b, OsModelBase)]
        if not parents:
            return new_class
        attr_meta = attrs.pop("Meta", None)
        abstract = getattr(attr_meta, "abstract", False)
        meta = attr_meta or getattr(new_class, "Meta", None)
        setattr(new_class, "_meta", Options(meta))
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
        fields = {}
        for obj_name, obj in attrs.items():
            if hasattr(obj, "__class__") and issubclass(obj.__class__, BaseField):
                fields[obj_name] = obj
        new_class._fields = fields
        registry.register(new_class)
        return new_class

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)

    @property
    def objects(cls) -> OsManager:
        if not hasattr(cls, "_objects"):
            cls._objects = OsManager(cls)
        return cls._objects

    @property
    def index_pattern(cls):
        return cls._meta.index_pattern

    @property
    def mapping(cls):
        mappings = {}
        for name, field in cls._fields.items():
            options = {"type": field.field_type}
            nests = name.split("_")
            if field.ignore_malformed:
                options["ignore_malformed"] = field.ignore_malformed
            unflatten(mappings, nests, options)
        return {"properties": mappings}

    @property
    def aliases(cls):
        return {}

    @property
    def settings(cls):
        return {"index": {}}

    @property
    def component_template(cls):
        return {
            "mappings": cls.mapping,
            "settings": cls.settings,
            "aliases": cls.aliases,
        }

    @property
    def abstract(cls):
        return cls._meta.abstract


class OsModel(metaclass=OsModelBase):
    """
    Nesting fields will be supported with dot notation
    """

    def save(self):
        pass

    @classmethod
    def create_index_mapping(cls):
        """
        Eventually it would be nice to handle this the same way
        django handles migrations. But will use this in the meantime
        as POC
        """
        client = OpenSearch(settings.OPENSEARCH_HOSTS)
        client.indices.create(index=cls.index_pattern, body=cls.component_template)
