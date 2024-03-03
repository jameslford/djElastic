from typing import List, Type

from ..base import OsModel


class CreateIndexMapping:

    def __init__(self, name: str, fields: List[tuple], options: dict) -> None:
        pass


def get_all_concrete_models() -> List[Type[OsModel]]:
    pass
