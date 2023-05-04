from sqladmin import ModelView

from app.users.models import Users
from app.bookings.models import Bookings


class UsersAdmin(ModelView, model=Users):
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False


class BookingsAdmin(ModelView, model=Bookings):
    name = "Бронь"
    name_plural = "Брони"
    icon = "fa-solid fa-book"
    column_list = [c.name for c in Bookings.__table__.c] + [Bookings.user]
