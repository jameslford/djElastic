from typing import TYPE_CHECKING, Type

from .queryset import OsQuerySet

if TYPE_CHECKING:
    from .models import OsModel


class OsManager:
    """
    We are going to forgo lots of the dynamism of Django's managers, as our concern is
    geared more towards a clear api and less towards a flexible one.

    For this same reason, we will enumerate all of the queryset methods here, as well
    as on the QuerySet. This is to make it clear what methods are available to the user,
    and allow legitimate type checking.
    """

    def __init__(self, model: Type["OsModel"]) -> None:
        self.model = model
        self.index = model.index_pattern

    def filter(self, *args, **kwargs) -> OsQuerySet:
        return OsQuerySet(self.model).filter(*args, **kwargs)

    def exclude(self, *args, **kwargs) -> OsQuerySet:
        return OsQuerySet(self.model).exclude(*args, **kwargs)

    def count(self) -> int:
        return OsQuerySet(self.model).count()

    def aggregate(self, *args, **kwargs):
        return OsQuerySet(self.model).aggregate(*args, **kwargs)

    def should(self, *args, **kwargs):
        return OsQuerySet(self.model).should(*args, **kwargs)

    def order_by(self, *args, **kwargs):
        return OsQuerySet(self.model).order_by(*args, **kwargs)

    def group_by(self, *args, **kwargs):
        return OsQuerySet(self.model).group_by(*args, **kwargs)

    def get(self, document_id):
        return OsQuerySet(self.model).get(document_id)

    def all(self) -> OsQuerySet:
        return OsQuerySet(self.model).all()
