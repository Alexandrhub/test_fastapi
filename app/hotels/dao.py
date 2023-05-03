from datetime import date

from sqlalchemy import select
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.database import async_session_maker, engine

class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def search_for_hotels(
        cls,
        location: str,
        date_from: date,
        date_to: date,
    ):
        async with async_session_maker() as session:
            get_hotels = select(Hotels)
            result = await session.execute(get_hotels)
            return result.scalar()
        



        # async with async_session_maker() as session:
        #     bookings_for_selected_dates = (
        #         select(Bookings)
        #         .filter(
        #             or_(
        #                 and_(
        #                     Bookings.date_from < date_from, Bookings.date_to > date_from
        #                 ),
        #                 and_(
        #                     Bookings.date_from >= date_from,
        #                     Bookings.date_from < date_to,
        #                 ),
        #         )
        #     ).subquery('filtered_bookings')
        # )
        
        # hotels_room_left = select(
        #     (
        #     Hotels.rooms_quantity - func.count(bookings_for_selected_dates.c.room_id)
        #     ).label('rooms_left'),
        #     Rooms.hotel_id,
        # ).select_from(Hotels).outerjoin(Rooms, Rooms.hotel_id == Hotels.id).outerjoin(
        #     bookings_for_selected_dates,
        #     bookings_for_selected_dates.c.room_id == Rooms.id,
        # ).where(
        #     Hotels.location.contains(location.title()),
        # ).group_by(Hotels.rooms_quantity, Rooms.hotel_id).cte('hotels_rooms_left')