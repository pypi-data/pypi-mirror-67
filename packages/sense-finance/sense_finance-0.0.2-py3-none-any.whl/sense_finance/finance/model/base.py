from django.db import models
from django.db import connections
import sense_core as sd


class BaseModel0(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True

    @classmethod
    def find_by_ids(cls, _ids):
        return cls.objects.filter(id__in=_ids).all()

    @classmethod
    def find_by_id(cls, id):
        try:
            return cls.objects.get(pk=id)
        except:
            return None

    @classmethod
    def find_many(cls, **kwargs):
        return cls.objects.filter(**kwargs).all()

    @classmethod
    def find_one(cls, **kwargs):
        try:
            item = cls.objects.get(**kwargs)
        except:
            item = None
        return item

    @classmethod
    def delete_by_id(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def find_all(cls):
        return cls.objects.all()

    @classmethod
    def batch_save(cls, items, batch_size=0):
        if not items:
            return
        if batch_size > 0:
            try:
                cls.objects.bulk_create(items, batch_size=batch_size)
                return
            except Exception as ex:
                sd.log_exception(ex)
        try:
            cls.objects.bulk_create(items)
            return
        except Exception as ex:
            sd.log_exception(ex)
        for data in items:
            try:
                data.save()
            except Exception as ex:
                sd.log_exception(ex)


class BaseModel(BaseModel0):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


@sd.try_catch_exception
def close_model_connection():
    connections.close_all()