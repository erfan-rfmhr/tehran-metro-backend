from contextlib import asynccontextmanager

from config.db import Database


async def on_startup():
    # on startup event for lifespan
    await Database.initialize()


async def on_shutdown():
    # on shutdown event for lifespan
    await Database().driver.close()


@asynccontextmanager
async def lifespan(app):
    await on_startup()
    yield
    await on_shutdown()
