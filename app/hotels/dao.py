from datetime import date

from sqlalchemy import func, select
from sqlalchemy.orm import sessionmaker
from app.database import engine, async_session_maker

from app.bookings.dao import BookingDAO
from app.dao.base import BaseDAO
from app.hotels.models import Hotels
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.models import Rooms
from app.hotels.schemas import SHotelsInfo


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_hotels_by_location(
        cls, location: str
    ) -> [SHotelsInfo]:
        result = []
        hotels = await cls.select_all_filter(
            func.lower(Hotels.location).like(f"%{location.lower()}%")
        )

        # # Create Session
        # Session = sessionmaker(bind=engine)
        # session = Session()
        #
        #
        # # search for available rooms for each hotel
        # for hotel in hotels:
        #     total_rooms = hotel.rooms.quantity
        #     session.expire_all()
        #     rooms = [
        #         room.id for room in await RoomsDAO.select_all_filter(Rooms.hotel_id == hotel.id)
        #     ]
        #
        #     # get all booked rooms for each hotel for date range
        #     count_booked_rooms = 0
        #     for room_id in rooms:
        #         count_booked_rooms += len(
        #             await BookingDAO.get_booking_rooms_by_id(room_id, date_from, date_to)
        #         )
        #     if total_rooms > count_booked_rooms:
        #         hotel.rooms_left = total_rooms - count_booked_rooms
        #         result.append(hotel)

        return hotels

    @classmethod
    async def find_all_hotels(cls) -> [SHotelsInfo]:
        hotels = await cls.select_all_filter_by()
        return hotels



