from app.dao.base import BaseDAO
from app.users.models import Users, UserAdmin


class UsersDAO(BaseDAO):
    model = Users


class UserAdminDAO(BaseDAO):
    model = UserAdmin
