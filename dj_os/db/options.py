class IndexMetaOptions:

    def __init__(self, meta: dict) -> None:
        self.managed = True
        self.meta = meta
        self.shards = 1
        self.replicas = 0
        self.index_pattern = None
