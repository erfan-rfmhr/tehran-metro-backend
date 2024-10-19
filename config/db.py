from neo4j import AsyncGraphDatabase

from config._settings import get_settings

settings = get_settings()


class Database:
    _instance = None
    _initialized = False
    _driver: AsyncGraphDatabase.driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self.__class__._initialized:
            return
        self.__class__._initialized = True

    @classmethod
    async def initialize(cls):
        if not cls._driver:
            cls._driver = AsyncGraphDatabase.driver(
                settings.NEO4J_URI,
                auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD),
            )
        await cls._driver.verify_connectivity()

    @property
    def driver(self) -> AsyncGraphDatabase.driver:
        if self.__class__._driver:
            return self.__class__._driver
        raise AttributeError("Driver not initialized")
