from pydantic_extra_types.phone_numbers import PhoneNumber
from fastapi_users import schemas
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[PhoneNumber] = None


class UserCreate(schemas.BaseUserCreate, UserBase):
    pass


class UserRead(schemas.BaseUser, UserBase):
    pass


class UserEdit(schemas.BaseUserUpdate, UserBase):
    pass
