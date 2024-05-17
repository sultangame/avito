from pydantic import BaseModel
from typing import Optional, List
from src.review.schemas import ReviewEnum


class ReviewRel(BaseModel):
    description: Optional[str] = None
    mark: Optional[ReviewEnum] = None


class ProductCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class ProductsRead(ProductCreate):
    id: int
    reviews: Optional[List[ReviewRel]] = None

    class Config:
        from_attributes = True


class ProductsEdit(ProductCreate):
    pass
