from fastapi import APIRouter
from src.users.router import router as user
from src.products.router import router as product


api = APIRouter(
    prefix="/api/v1"
)
api.include_router(user)
api.include_router(product)
