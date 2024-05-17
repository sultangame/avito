from sqlalchemy import select
from src.service.depends import detail_or_404
from src.database import async_session_maker


async def find_one_with_second(pk: int, model, second: int, join):
    async with async_session_maker() as session:
        stmt = select(model).where(join == second).where(model.id == pk)
        result = await session.execute(stmt)
        return await detail_or_404(detail=result.scalar())


async def find_one(pk: int, model):
    async with async_session_maker() as session:
        stmt = select(model).where(model.id == pk)
        result = await session.execute(stmt)
        return await detail_or_404(result.scalar())
