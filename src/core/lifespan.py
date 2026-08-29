from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.settings import Settings

from src.core.container import Container


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.settings = Settings()

    app.state.container = Container(app.state.settings)
    yield