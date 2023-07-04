from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.rooms.dao import RoomsDAO

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
@cache(expire=20)
async def get_all_rooms_by_hotel_id(hotel_id: str, data_from: date, data_to: date):
    """Returns all available rooms by hotel id between date_from - date_to."""
    return await RoomsDAO.get_available_rooms_by_hotel_id(int(hotel_id), data_from, data_to)
