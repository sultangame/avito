from fastapi_users import FastAPIUsers
from fastapi import APIRouter, Depends
from .manager import get_user_manager
from .models import UserORM
from .backend import auth_backend
from .schemas import UserRead, UserCreate, UserEdit
from .repository import user_service
from typing import Annotated

from ..service import BaseService

fastapi_users = FastAPIUsers[UserORM, int](
    get_user_manager,
    [auth_backend]
)
router = APIRouter(
    prefix="/users",
    tags=["account"]
)

current_user = fastapi_users.current_user(active=True)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
)


@router.get("/current/user/me/")
async def get_current_user(
    service: Annotated[BaseService, Depends(user_service)],
    user: UserORM = Depends(current_user),
):
    user = await service.find_one(pk=user.id)
    return user


@router.patch("/edit/current/user/")
async def edit_current_user(
        service: Annotated[BaseService, Depends(user_service)],
        model: UserEdit,
        user: UserORM = Depends(current_user)
):
    user = await service.edit_one(schemas=model, pk=user.id)
    return user
