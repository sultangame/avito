from src.service import BaseService
from .crud import reviews_service
from fastapi import APIRouter, Depends
from typing import Annotated, List
from .schemas import ReviewAdd, ReviewRead
from src.specific import find_one
from src.products import ProductsORM
from .models import ReviewORM

router = APIRouter(
    prefix="/reviews",
    tags=["review"]
)


@router.post("/add/new/review/")
async def add_new_review(
        schemas: ReviewAdd,
        service: Annotated[BaseService, Depends(reviews_service)],
        pk: int
):
    product = await find_one(pk=pk, model=ProductsORM)
    if product:
        answer = ReviewORM(**schemas.model_dump())
        answer.product.append(product)
        new_review = await service.add_one(data=answer)
        return new_review
    return product


@router.get(
    "/find/all/reviews/",
    response_model=List[ReviewRead]
)
async def find_all_reviews(service: Annotated[BaseService, Depends(reviews_service)]):
    reviews = await service.find_all(selectin=ReviewORM.product)
    return reviews
