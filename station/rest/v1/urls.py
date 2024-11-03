from fastapi import APIRouter

from station.rest.v1.routers.details import v1_details_router

v1_router = APIRouter(prefix="/v1", tags=["v1", "stations"])

v1_router.include_router(v1_details_router)

__all__ = ["v1_router"]
