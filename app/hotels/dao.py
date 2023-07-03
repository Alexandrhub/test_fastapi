from datetime import date

from sqlalchemy import select, func, literal

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


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


    @classmethod
    async def find_hotels_in_rooms_all(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = select(Hotels).filter_by(hotel_id=hotel_id)
            all_rooms_execute = await session.execute(query)
            all_rooms = all_rooms_execute.mappings().all()

            results = []
            for room in all_rooms:
                room_id = room["id"]

                booked_room = (
                    select(Bookings)
                    .where(
                        (Bookings.room_id == room_id)
                        & (Bookings.date_to >= date_to)
                        & (Bookings.date_from <= date_from)
                    )
                    .cte("booked_room")
                )

                get_room_available = (
                    (
                        select(Rooms.quantity - func.count(booked_room.c.room_id)).label(
                            "room_available"
                        ),
                        ((literal(date_to) - literal(date_from)) * Bookings.price).label(
                            "total_price"
                        ),
                    )
                    .select_from(Hotels)
                    .join(booked_room, booked_room.c.room_id == Hotels.id, isouter=True)
                    .where(Hotels.id == room_id)
                    .group_by(Rooms.quantity, booked_room.c.room_id, Rooms.price)
                )

                room_available_execute = await session.execute(get_room_available)
                room_available = room_available_execute.mappings().one()
                res = {**room, **room_available}
                results.append(res)

            return results


