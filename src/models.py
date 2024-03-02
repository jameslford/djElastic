from .managers import EsManager


class EsModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = None
        return new_class

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        required_attrs = ["index_pattern"]
        for attr in required_attrs:
            if attr not in attrs:
                raise ValueError(f"EsModel must define {attr}")

    @property
    def objects(cls) -> EsManager:
        if not hasattr(cls, "_objects"):
            cls._objects = EsManager(cls)
        return cls._objects


class EsModel(metaclass=EsModelBase):
    pass
