from fastapi import FastAPI

from config.utils import lifespan
from station.rest.urls import station_router

app = FastAPI(lifespan=lifespan)

app.include_router(station_router)
