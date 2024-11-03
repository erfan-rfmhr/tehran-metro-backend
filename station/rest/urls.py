from fastapi import APIRouter

from station.rest.v1.urls import v1_router

station_router = APIRouter(prefix="/stations", tags=["station"])

station_router.include_router(v1_router)

__all__ = ["station_router"]
