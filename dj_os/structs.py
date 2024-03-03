from typing import List

from opensearchpy.helpers.response import Response


class OsResults:
    def __init__(self, results: Response):
        self.results = results

    @property
    def hits(self) -> int:
        return self.results.hits

    @property
    def aggregations(self) -> List[dict]:
        """ """
        return self.results.aggregations

    @property
    def source(self) -> List[dict]:
        return self.results.to_dict()
