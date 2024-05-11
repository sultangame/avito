from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from src.database import Model
from .schemas import ReviewEnum
from src.database.secondary import products_review


class ProductsORM(Model):
    __tablename__ = "products"
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    review: Mapped[list["ReviewsORM"]] = relationship(
        back_populates="product", secondary=products_review
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("user.id", ondelete="CASCADE")
    )


class ReviewsORM(Model):
    __tablename__ = "reviews"
    product: Mapped[list["ProductsORM"]] = relationship(
        back_populates="review", secondary=products_review
    )
    text: Mapped[str] = mapped_column(String)
    review: Mapped["ReviewEnum"] = mapped_column(default=ReviewEnum.NONE)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
