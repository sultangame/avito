from fastapi import APIRouter
from src.products.router import router as product


api = APIRouter(
    prefix="/api/v1"
)
api.include_router(product)
