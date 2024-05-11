from enum import Enum

from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class ProductsRead(ProductCreate):
    id: int

    class Config:
        from_attributes = True


class ProductsEdit(ProductCreate):
    pass


class ReviewEnum(Enum):
    NONE = "NONE"
    BAD = "BAD"
    NOT_VERY = "NOT_VERY"
    GOOD = "GOOD"
