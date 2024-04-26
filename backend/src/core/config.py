import os
from collections.abc import AsyncIterator
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
async def lifespan(application: FastAPI) -> AsyncIterator:
    await Tortoise.init(TORTOISE_ORM)
    try:
        yield
    finally:
        await Tortoise.close_connections()
