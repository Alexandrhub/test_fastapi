from sqlalchemy import delete, insert, select

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def select_all_filter(cls, *args):
        async with async_session_maker() as session:
            query = select(cls.model).filter(*args)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def select_all_filter_by(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def select_one_or_none_filter(cls, *args):
        async with async_session_maker() as session:
            query = select(cls.model).filter(*args)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def select_one_or_none_filter_by(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
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
    async def delete_rows_filer(cls, *args) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).filter(*args)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete_rows_filer_by(cls, **kwargs) -> None:
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**kwargs)
            await session.execute(query)
            await session.commit()
