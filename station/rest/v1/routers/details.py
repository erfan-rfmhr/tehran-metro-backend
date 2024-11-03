from fastapi import APIRouter

from station.manager import StationManager
from station.rest.v1.schemas.base import Station

v1_details_router = APIRouter(prefix="/details")


@v1_details_router.get("/{name}/", response_model=Station)
async def get_details(name: str):
    station_details = await StationManager.get_station_by_name(name)
    return station_details
