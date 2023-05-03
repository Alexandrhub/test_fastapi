import asyncio

from datetime import date, datetime
from typing import List, Optional
from pydantic import parse_obj_as

from fastapi import APIRouter, Query

from app.hotels.dao import HotelsDAO
from app.hotels.schemas import HotelInfo
from fastapi_cache.decorator import cache

router = APIRouter(prefix='/hotels', tags=['Отели'])


@router.get('/{location}')
@cache(expire=60)
async def get_hotels_by_location_and_time(
    location: str,
    date_from: date=Query(..., description=f'Например, {datetime.now().date()}'),
    date_to: date=Query(..., description=f'Например, {datetime.now().date()}'),
):
    await asyncio.sleep(3)
    hotels = await HotelsDAO.find_all()
    return hotels