from src.repository import SQLAlchemyRepository
from .models import ProductsORM
from src.service import BaseService


class ProductsRepository(SQLAlchemyRepository):
    model = ProductsORM


def product_service():
    return BaseService(ProductsRepository)
