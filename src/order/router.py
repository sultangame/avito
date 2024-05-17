from fastapi import APIRouter, Depends
from .crud import order_service
from src.service import BaseService
from typing import Annotated, List
from . import schemas
from .models import OrderORM
from src.specific import find_one
from ..products import ProductsORM

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.get(
    "/get/all/orders/",
    response_model=List[schemas.OrderRead]
)
async def get_all_orders(
        service: Annotated[BaseService, Depends(order_service)]
):
    orders = await service.find_all(selectin=OrderORM.product)
    return orders


@router.get(
    "/get/one/order/{pk}/",
    response_model=schemas.OrderRead
)
async def get_one_order(
        pk: int,
        service: Annotated[BaseService, Depends(order_service)]
):
    order = await service.find_one(pk=pk, selectin=OrderORM.product)
    return order


@router.post(
    "/add/new/order/",
    response_model=schemas.OrderAdd
)
async def add_new_order(
        pk: int,
        data: schemas.OrderAdd,
        service: Annotated[BaseService, Depends(order_service)]
):
    product = await find_one(pk=pk, model=ProductsORM)
    new_order = OrderORM(**data.model_dump(exclude_unset=True))
    new_order.product.append(product)
    result = await service.add_one(data=new_order)
    return result


@router.delete("/delete/one/order/{pk}")
async def delete_order(
        pk: int,
        service: Annotated[BaseService, Depends(order_service)]
):
    result = await service.delete_one(pk=pk, selectin=OrderORM.product)
    return result
