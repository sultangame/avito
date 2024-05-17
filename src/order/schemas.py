from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProductRel(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None


class OrderAdd(BaseModel):
    promo: Optional[str] = None
    created_at: datetime = datetime.utcnow()


class OrderRead(OrderAdd):
    id: int
    product: Optional[List["ProductRel"]] = None
