from fastapi import APIRouter
from src.products.router import router as product
from src.review.router import router as review
from src.order.router import router as order


api = APIRouter(
    prefix="/api/v1"
)
api.include_router(product)
api.include_router(review)
api.include_router(order)
