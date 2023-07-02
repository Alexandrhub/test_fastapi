from sqlalchemy import select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def search_hotels_by_name(cls, name: str):
        async with async_session_maker() as session:
            get_hotels = select(Hotels).where(Hotels.name.ilike(f"%{name}%"))
            result = await session.execute(get_hotels)
            return result.scalars().all()

    @classmethod
    async def search_for_hotels(cls, location: str):
        async with async_session_maker() as session:
            get_hotels = select(Hotels).where(Hotels.location.ilike(f"%{location}%"))
            result = await session.execute(get_hotels)
            return result.scalars().all()
