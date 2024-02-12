import inspect
from functools import wraps
from typing import TYPE_CHECKING, Type

from .queryset import EsQuerySet

if TYPE_CHECKING:
    from .models import EsModel


class EsManager:
    """
    We are going to forgo lots of the dynamism of Django's managers, as our concern is
    geared more towards a clear api and less towards a flexible one.

    For this same reason, we will enumerate all of the queryset methods here, as well
    as on the QuerySet. This is to make it clear what methods are available to the user,
    and allow legitimate type checking.
    """

    def __init__(self, model: Type["EsModel"]) -> None:
        self.model = model
        self.index = model.index_pattern

    def filter(self, *args, **kwargs) -> EsQuerySet:
        return EsQuerySet(self.model).filter(*args, **kwargs)

    def exclude(self, *args, **kwargs) -> EsQuerySet:
        return EsQuerySet(self.model).exclude(*args, **kwargs)

    def count(self) -> int:
        return EsQuerySet(self.model).count()

    def aggregate(self, *args, **kwargs):
        return EsQuerySet(self.model).aggregate(*args, **kwargs)

    def should(self, *args, **kwargs):
        return EsQuerySet(self.model).should(*args, **kwargs)

    def order_by(self, *args, **kwargs):
        return EsQuerySet(self.model).order_by(*args, **kwargs)

    def group_by(self, *args, **kwargs):
        return EsQuerySet(self.model).group_by(*args, **kwargs)

    def get(self, document_id):
        return EsQuerySet(self.model).get(document_id)

    def all(self) -> EsQuerySet:
        return EsQuerySet(self.model).all()
