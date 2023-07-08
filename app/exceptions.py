from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Пользователь уже существует",)


class IncorrectEmailOrPasswordException(BookingException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Неверная почта или пароль",)


class TokenExpiredException(BookingException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Токен истек",)


class TokenAbsentException(BookingException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Токен отсутствует",)


class IncorrectTokenException(BookingException):
    status_code = (status.HTTP_401_UNAUTHORIZED,)
    detail = ("Неверный формат токена",)


class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserIsNotAdminException(BookingException):
    status_code = (status.HTTP_403_FORBIDDEN,)
    detail = ("Пользователь не является администратором",)


class RoomCannotBeBookedException(BookingException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Не осталось свободных номеров",)


class DateFromWrongFormatException(BookingException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Неверный формат даты, date_from >= date_to",)


class BookingDoesNotExistException(BookingException):
    status_code = (status.HTTP_404_NOT_FOUND,)
    detail = ("Брони не существует",)


class OutOfDateException(BookingException):
    status_code = (status.HTTP_409_CONFLICT,)
    detail = ("Неверные параметры даты",)
