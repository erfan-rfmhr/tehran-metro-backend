from contextlib import asynccontextmanager

from config.db import get_driver, verify_db


async def on_startup():
    # on startup event for lifespan
    await verify_db()


async def on_shutdown():
    # on shutdown event for lifespan
    driver = await get_driver()
    await driver.close()


@asynccontextmanager
async def lifespan(app):
    await on_startup()
    yield
    await on_shutdown()
