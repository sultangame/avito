from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from src.database import Model
from typing import TYPE_CHECKING, List
from src.database.secondary import products_review
if TYPE_CHECKING:
    from src.review import ReviewORM


class ProductsORM(Model):
    __tablename__ = "products"
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    reviews: Mapped[List["ReviewORM"]] = relationship(
        back_populates="product", secondary=products_review
    )
