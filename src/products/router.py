from fastapi import APIRouter, Depends, status
from typing import Annotated
from src.service import BaseService
from .crud import product_service
from . import schemas
from .models import ProductsORM


router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get(
    "/get/all/products/",
    response_model=list[schemas.ProductsRead]
)
async def get_all_products(
        service: Annotated[BaseService, Depends(product_service)]
):
    answer = await service.find_all(selectin=ProductsORM.reviews)
    return answer


@router.get(
    "/get/one/product/{pk}/",
    response_model=schemas.ProductsRead
)
async def get_one_product(
        pk: int,
        service: Annotated[BaseService, Depends(product_service)]
):
    answer = await service.find_one(pk=pk, selectin=ProductsORM.reviews)
    return answer


@router.post(
    "/add/new/product/",
    response_model=schemas.ProductCreate,
    status_code=status.HTTP_201_CREATED
)
async def add_new_product(
        model: schemas.ProductCreate,
        service: Annotated[BaseService, Depends(product_service)]
):
    product = ProductsORM(**model.model_dump())
    answer = await service.add_one(data=product)
    return answer


@router.patch(
    "/edit/one/product/{pk}/",
    response_model=schemas.ProductsRead
)
async def edit_one_product(
        pk: int,
        model: schemas.ProductsEdit,
        service: Annotated[BaseService, Depends(product_service)]
):
    result = await service.edit_one(schemas=model, pk=pk)
    return result


@router.delete("/delete/one/product/{pk}")
async def delete_one_product(
        pk: int,
        service: Annotated[BaseService, Depends(product_service)]
):
    answer = await service.delete_one(pk=pk, selectin=ProductsORM.reviews)
    return answer
