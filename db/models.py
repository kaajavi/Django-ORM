import sys
from async_models.models import AbstractAsyncModel
try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()

# Sample User model
class User(AbstractAsyncModel):
    name = models.CharField(max_length=50, default="Dan")

    def __str__(self):
        return self.name

