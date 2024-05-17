from src.service import BaseService
from src.repository import SQLAlchemyRepository
from .models import OrderORM


class OrderRepository(SQLAlchemyRepository):
    model = OrderORM


def order_service():
    return BaseService(OrderRepository)
