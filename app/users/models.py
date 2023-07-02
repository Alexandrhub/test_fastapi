from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    booking = relationship("Bookings", back_populates="user")

    def __str__(self) -> str:
        return f"Пользователь {self.email}"


class UserAdmin(Base):
    __tablename__ = "user_admin"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def __str__(self) -> str:
        return f"Администратор {self.email}"
