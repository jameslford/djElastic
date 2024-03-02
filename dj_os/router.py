from importlib import import_module

from django.conf import settings


class OsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == "es":
            return "es"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "es":
            return "es"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == "es" or obj2._meta.app_label == "es":
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "es":
            return db == "es"
        return None


def get_router():
    if settings.DJ_ES_ROUTER:
        module, klass = settings.DJ_ES_ROUTER.rsplit(".", 1)
        mod = import_module(module)
        return getattr(mod, klass)
    return OsRouter
