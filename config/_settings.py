from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NEO4J_URI: str = "neo4j://localhost:7687"
    NEO4J_USERNAME: str = "neo4j"
    NEO4J_PASSWORD: str = "12345678"
    DB_NAME: str = "subway"


@lru_cache
def get_settings():
    return Settings()
