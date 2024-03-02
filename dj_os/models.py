from .managers import OsManager


class OsModelBase(type):
    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        new_class._meta = None
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
    pass
