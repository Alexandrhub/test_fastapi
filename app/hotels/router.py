import asyncio
from datetime import date, datetime

from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from app.hotels.dao import HotelsDAO

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/locations")
@cache(expire=60)
async def get_hotels_by_location(location: str):
    hotels = await HotelsDAO.search_for_hotels(location=location)
    return hotels


@router.get("")
async def get_hotels_by_name(name):
    hotels = await HotelsDAO.search_hotels_by_name(name)
    return hotels
