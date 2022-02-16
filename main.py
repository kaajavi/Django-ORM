############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

############################################################################
## Config FastAPI
############################################################################

from fastapi import FastAPI

app = FastAPI()

############################################################################
## START OF APPLICATION
############################################################################
from db.models import *

@app.on_event("startup")
async def startup_event():
    await User.objects.async_create(name='Dan')
    await User.objects.async_create(name='Robert')



@app.get("/")
async def root():
    users = await User.objects.async_all()
    return {"users": list(users.values('name'))}




