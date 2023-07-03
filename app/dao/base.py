from sqlalchemy import insert, select, delete

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all_filter(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter(*args, **kwargs)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_all_filter_by(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(*args, **kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none_filter(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter(*args, **kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none_filter_by(cls, *args, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(*args, **kwargs)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add_rows(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result

    @classmethod
    async def delete_rows_filter(cls, *args, **kwargs) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).filter(*args, **kwargs)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_rows_filter_by(cls, *args, **kwargs) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(*args, **kwargs)
            await session.execute(query)
            await session.commit()
