from django.db.models import Model
from async_models.manager import AsyncManager

class AbstractAsyncModel(Model):
    objects = AsyncManager()

    class Meta:
        abstract = True

