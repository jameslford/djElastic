from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type

from dateutil.parser import parse
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Q, Search
from elasticsearch_dsl.field import Boolean as BooleanField
from elasticsearch_dsl.field import Date as DateField
from elasticsearch_dsl.field import Float as FloatField
from elasticsearch_dsl.field import Integer as IntegerField
from elasticsearch_dsl.field import Ip as IpField
from elasticsearch_dsl.field import Keyword as KeywordField
from elasticsearch_dsl.field import Long as LongField
from elasticsearch_dsl.field import Text as TextField

if TYPE_CHECKING:
    from src.models import EsModel

RANGE_FIELDS = [
    DateField,
    IntegerField,
    LongField,
    FloatField,
    IpField,
]

from typing import Literal

from elasticsearch_dsl import A

ScheduleType = Literal["minute", "hour", "day", "week", "month", "quarter", "year"]


def dt_to_es_format(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class BaseSearch:
    def __init__(self, model: Type["EsModel"], search: Optional[Search] = None):
        self.model = model
        self.index = model._meta.index_pattern
        self._body = search.to_dict() if search else {}
        self._search = search

    @property
    def search(self) -> Search:
        if self._search is None:
            self._search = Search(
                using=self.model._client, index=self.model._meta.index_pattern
            )
        return self._search

    @search.setter
    def search(self, value: Search) -> None:
        self._search = value

    def filter(self, **kwargs) -> "BaseSearch":
        """
        Return a new EsQuerySet instance with the args ANDed to the existing
        set.
        """
        for k, v in kwargs.items():
            modifier_split = k.split("__")
            modifier = None
            if len(modifier_split) > 1:
                k = modifier_split[0]
                modifier = modifier_split[1]

            field_type = self.model.get_field_type(k)

            if modifier == "in":
                if not isinstance(v, list):
                    raise ValueError(f"Expected list for {k}__in")
                self.search = self.search.filter("terms", **{k: v})
                continue
            if field_type in RANGE_FIELDS:
                if modifier is None:
                    if isinstance(v, datetime):
                        v = dt_to_es_format(v)
                    self.search = self.search.filter("term", **{k: v})
                self.search = self.search.filter("range", **{k: {modifier: v}})
                continue
            self.search = self.search.filter("term", **{k: v})
        return self

    def match(self, **kwargs) -> "BaseSearch":
        """
        Return a new EsQuerySet instance with the args ANDed to the existing
        set.
        """
        for k, v in kwargs.items():
            self.search = self.search.query("match", **{k: v})
        return self

    def count(self) -> int:
        return self.search.count()

    def should(self, **kwargs) -> "BaseSearch":
        for k, v in kwargs.items():
            self.search = self.search.query("match", **{k: v})
        return self
