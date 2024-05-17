from sqlalchemy.orm import selectinload
from abc import ABC, abstractmethod
from src.database import async_session_maker
from sqlalchemy import select, update, delete


class AbstractRepository(ABC):
    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self):
        raise NotImplementedError

    @abstractmethod
    async def edit_one(self):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def find_all(self, selectin):
        async with async_session_maker() as session:
            stmt = select(self.model).order_by(self.model.id).options(
                selectinload(selectin)
            )
            result = await session.execute(stmt)
            return result.scalars().all()

    async def find_one(self, pk: int, selectin):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == pk).options(
                selectinload(selectin)
            )
            result = await session.execute(stmt)
            return result.scalar()

    async def add_one(self, data):
        async with async_session_maker() as session:
            session.add(data)
            await session.commit()
            await session.refresh(data)
            return data

    async def delete_one(self, pk: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(self.model).where(self.model.id == pk)
            await session.execute(stmt)
            await session.commit()

    async def edit_one(self, data: dict, pk: int) -> None:
        async with async_session_maker() as session:
            stmt = update(self.model).where(self.model.id == pk).values(**data)
            await session.execute(stmt)
            await session.commit()