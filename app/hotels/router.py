from fastapi import APIRouter

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import SHotelsInfo

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{location}")
async def get_hotels_by_location(location: str):
    """Get hotels by location"""
    hotels = await HotelsDAO.find_hotels_by_location(location)
    return hotels


@router.get("/all")
async def get_all_hotels():
    """Get all hotels."""
    hotels = await HotelsDAO.select_all()
    return hotels


@router.get("/{hotel_id}")
async def get_hotel_by_id(hotel_id: int) -> SHotelsInfo:
    """Get hotel by id."""
    hotel = await HotelsDAO.select_one_or_none_filter_by(id=hotel_id)
    return hotel
