from functools import lru_cache

from neo4j import AsyncGraphDatabase, AsyncSession

from config._settings import get_settings

settings = get_settings()

_driver = AsyncGraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
)


@lru_cache
async def get_driver():
    return _driver


async def verify_db():
    await _driver.verify_connectivity()
    await _driver.verify_authentication()


@lru_cache
def get_session() -> AsyncSession:
    session = _driver.session(database=settings.DB_NAME)
    return session
