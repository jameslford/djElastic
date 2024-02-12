from typing import TYPE_CHECKING, List, Optional, Type, Union

import pandas as pd
from django.conf import settings
from elasticsearch_dsl import Search

if TYPE_CHECKING:
    from .models import EsModel


class EsQuerySet:

    def __init__(self, model: Type["EsModel"], search: Optional[Search] = None):
        self.model = model
        self.index = model._meta.index_pattern
        self.search = search or Search(index=self.index)
        self._source = None
        self._cached_results = None

    @property
    def host(self):
        if self.search._using is not None:
            return self.search._using.host
        return settings.ELASTICSEARCH["default"]["host"]

    @property
    def port(self):
        if self.search._using is not None:
            return self.search._using.port
        return settings.ELASTICSEARCH["default"]["port"]

    @property
    def client(self):
        pass

    @property
    def write_client(self):
        pass

    def execute_read(self):
        results = self.search.using(self.client).index(self.index).execute()
        self._cached_results = results.to_dict()
        return results

    def clone(self):
        return EsQuerySet(self.model, search=self.search)

    def to_dict(self):
        queries = self.search.to_dict()
        return

    def range(self, field, gte=None, lte=None, gt=None, lt=None):
        """
        Add a range filter to the query.
        """
        search_dict = {}
        if gte is not None:
            search_dict["gte"] = gte
        if lte is not None:
            search_dict["lte"] = lte
        if gt is not None:
            search_dict["gt"] = gt
        if lt is not None:
            search_dict["lt"] = lt
        self.search = self.search.filter("range", **{field: search_dict})
        return self

    def filter(self, *args, **kwargs):
        """
        This is a term or terms filter that will be added to the query.
        The default query is a term query (`{'term': 'field': 'value'}`), but if the key is suffixed with __in, then
        the query will be a terms query.
        """
        for arg in args:
            self.search = self.search.filter(arg)
        for key, value in kwargs.items():
            modifier_split = value.split("__")
            modifier = None
            if len(modifier_split) > 1:
                modifier = modifier_split[-1]
            if modifier == "in":
                self.search = self.search.filter("terms", **{key: value})
            else:
                self.search = self.search.filter("term", **{key: value})
        return self

    def exclude(self, *args, **kwargs):
        pass

    def count(self):
        pass

    def aggregate(self, *args, **kwargs):
        pass

    def should(self, *args, **kwargs):
        pass

    def order_by(self, *args, **kwargs):
        pass

    def group_by(self, *args, **kwargs):
        pass

    def get(self, document_id):
        pass

    def all(self):
        pass

    def only(self, *args):
        self._source = args

    def size(self, size):
        self.search = self.search[:size]

    def values(self, *args, **kwargs):
        """
        Executes the query and returns the results as a list of dictionaries.
        While only the partial results are returned, the query is executed in full,
        and the results are cached.
        """
        pass

    def values_list(self, *args, distinct=False):
        """
        Executes the query and returns the results as a list.
        While only the partial results are returned, the query is executed in full,
        and the results are cached.

        If distinct is True, the results will be unique.
        """

    ######################
    # Methods that do not return a new queryset
    ######################
    def create(self, records: Union[List | List[dict]]):
        """
        Will add one or more records to the index.
        """

    def update(self):
        """
        This API does not support updating records.
        This is only provided for consistency with Django's ORM.
        """
        raise NotImplementedError("djElastic does not support updating records.")

    def delete(self):
        """
        This API does not support deleting records.
        This is only provided for consistency with Django's ORM.
        """
        raise NotImplementedError("djElastic does not support deleting records.")
