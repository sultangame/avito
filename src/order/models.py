from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List
from src.database.secondary import orders_products
from src.database import Model
from datetime import datetime
if TYPE_CHECKING:
    from src.products import ProductsORM


class OrderORM(Model):
    __tablename__ = "orders"
    promo_code: Mapped[str | None] = mapped_column(String, nullable=True)
    product: Mapped[List["ProductsORM"]] = relationship(
        back_populates="order", secondary="orders_products"
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
