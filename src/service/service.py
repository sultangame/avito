from pydantic import BaseModel

from src.repository import AbstractRepository
from .depends import detail_or_404


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def find_all(self):
        result = await self.repository.find_all()
        return result

    async def find_one(self, pk: int):
        result = await self.repository.find_one(pk=pk)
        return await detail_or_404(detail=result)

    async def add_one(self, data: dict):
        result = await self.repository.add_one(data=data)
        return result

    async def edit_one(self, schemas: BaseModel, pk: int, partial: bool = True):
        data = schemas.model_dump(exclude_unset=partial)
        detail = await self.find_one(pk=pk)
        if detail:
            await self.repository.edit_one(data=data)
            return await self.find_one(pk=pk)
        return detail

    async def delete_one(self, pk: int):
        detail = await self.find_one(pk=pk)
        if detail:
            await self.repository.delete_one(pk=pk)
            return {"Message": "Deleted successful"}
        return detail
