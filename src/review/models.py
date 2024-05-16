from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING, List
from sqlalchemy import String
from .schemas import ReviewEnum
from src.database import Model
from src.database.secondary import products_review
if TYPE_CHECKING:
    from src.products import ProductsORM


class ReviewORM(Model):
    __tablename__ = "reviews"
    product: Mapped[List["ProductsORM"]] = relationship(
        back_populates="reviews", secondary=products_review
    )
    description: Mapped[str] = mapped_column(String)
    mark: Mapped["ReviewEnum"] = mapped_column(
        default=ReviewEnum.NONE, nullable=False
    )
