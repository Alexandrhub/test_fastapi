from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotelsInfo, SHotelsRoomsLeft

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{location}")
async def get_hotels_by_location(
    location: str, date_from: date, date_to: date
) -> list[SHotelsRoomsLeft]:
    """Get hotels by location and available date range and rooms left."""
    hotels = await HotelsDAO.find_hotels_by_location(location, date_from, date_to)
    return hotels


@router.get("/all")
@cache(expire=30)
async def get_all_hotels() -> list[SHotelsInfo]:
    """Get all hotels."""
    hotels = await HotelsDAO.select_all_filter()
    return hotels


@router.get("/id")
@cache(expire=30)
async def get_hotel_by_id(hotel_id: int) -> SHotelsInfo:
    """Get hotel by id."""
    hotel = await HotelsDAO.select_one_or_none_filter_by(id=hotel_id)
    return hotel
