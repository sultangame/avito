from src.repository import SQLAlchemyRepository
from src.service import BaseService
from .models import UserORM


class UserRepository(SQLAlchemyRepository):
    model = UserORM


def user_service():
    return BaseService(UserRepository)
