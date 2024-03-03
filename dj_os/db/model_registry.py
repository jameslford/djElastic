class ModelRegistry:
    def __init__(self):
        self.models = {}
        self.concrete_models = {}

    def register(self, model):
        self.models[model.__name__] = model
        if not model._meta.abstract:
            self.concrete_models[model.__name__] = model

    @property
    def indices_used(self):
        return [model._meta.index_pattern for model in self.concrete_models.values()]

    def get(self, model_name):
        return self.models[model_name]


registry = ModelRegistry()
