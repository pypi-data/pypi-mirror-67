from sense_finance.finance.common.constant0 import FINANCE_DB


class ModelRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == FINANCE_DB:
            return FINANCE_DB
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model)

    def allow_relation(self, obj1, obj2, **hints):
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return False
