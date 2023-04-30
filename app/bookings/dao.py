from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.bookings.models import Bookings

from sqlalchemy import select


class BookingDAO(BaseDAO):
    model = Bookings
    
