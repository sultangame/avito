from pydantic import BaseModel
from src.specific import find_one
from src.repository import AbstractRepository
from .depends import detail_or_404


class BaseService:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def find_all(self, selectin):
        result = await self.repository.find_all(selectin=selectin)
        return result

    async def find_one(self, pk: int, selectin):
        result = await self.repository.find_one(pk=pk, selectin=selectin)
        return await detail_or_404(detail=result)

    async def add_one(self, data):
        result = await self.repository.add_one(data=data)
        return result

    async def edit_one(self, schemas: BaseModel, pk: int, partial: bool = True):
        data = schemas.model_dump(exclude_unset=partial)
        detail = await self.find_one(pk=pk)
        if detail:
            await self.repository.edit_one(data=data)
            return await self.find_one(pk=pk)
        return detail

    async def delete_one(self, pk: int, selectin):
        detail = await self.find_one(pk=pk, selectin=selectin)
        if detail:
            await self.repository.delete_one(pk=pk)
            return {"Message": "Deleted successful"}
        return detail
