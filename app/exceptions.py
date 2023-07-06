from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует",
)

IncorrectEmailOrPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверная почта или пароль",
)

TokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен истек",
)

TokenAbsentException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Токен отсутствует",
)

IncorrectTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Неверный формат токена",
)

UserIsNotPresentException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

UserIsNotAdminException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Пользователь не является администратором",
)

RoomCannotBeBookedException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Не осталось свободных номеров",
)
DateFromWrongFormatException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Неверный формат даты, date_from >= date_to",
)

BookingDoesNotExistException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Брони не существует",
)

OutOfDateException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Неверные параметры даты",
)
