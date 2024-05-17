from src.repository import SQLAlchemyRepository
from .models import ReviewORM
from src.service import BaseService


class ReviewRepository(SQLAlchemyRepository):
    model = ReviewORM


def reviews_service():
    return BaseService(ReviewRepository)
