from typing import Optional, List

from pydantic import BaseModel
from enum import Enum


class ReviewEnum(Enum):
    NONE: str = "NONE"
    BAD: str = "BAD"
    NOT_VERY: str = "NOT_VERY"
    GOOD: str = "GOOD"


class ProductRel(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class ReviewAdd(BaseModel):
    description: str
    mark: Optional[ReviewEnum] = None


class ReviewRead(ReviewAdd):
    id: int
    product: Optional[List["ProductRel"]] = None
