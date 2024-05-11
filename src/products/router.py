from fastapi import APIRouter, Depends
from typing import Annotated
from src.service import BaseService
from .repository import product_service
from . import schemas


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
    answer = await service.find_all()
    return answer


@router.get(
    "/get/one/product/{pk}/",
    response_model=schemas.ProductsRead
)
async def get_one_product(
        pk: int,
        service: Annotated[BaseService, Depends(product_service)]
):
    answer = await service.find_one(pk=pk)
    return answer


@router.post(
    "/add/new/product/",
    response_model=schemas.ProductsRead
)
async def add_new_product(
        model: schemas.ProductCreate,
        service: Annotated[BaseService, Depends(product_service)]
):
    answer = await service.add_one(data=model.model_dump())
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
    answer = await service.delete_one(pk=pk)
    return answer
