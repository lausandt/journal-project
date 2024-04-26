import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from tortoise import Tortoise

TORTOISE_ORM = {
    'connections': {'default': os.environ.get('DATABASE_URL')},
    'apps': {
        'models': {'models': ['src.core.models', 'aerich.models'], 'default_connection': 'default'}
    },
}


@asynccontextmanager
async def lifespan(application: FastAPI):
    await Tortoise.init(TORTOISE_ORM)
    yield
    await Tortoise.close_connections()
