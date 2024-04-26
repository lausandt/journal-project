from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import lifespan

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8080'],  # frontend
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def root() -> dict[str, str]:
    return {'Message': 'George is an async rhino, very lazy indeed!'}
