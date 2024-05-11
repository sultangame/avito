from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from src.database import Model


class ProductsORM(Model):
    __tablename__ = "products"
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
