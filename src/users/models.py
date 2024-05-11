from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Model, get_async_session
from fastapi import Depends
from sqlalchemy import String


class UserORM(SQLAlchemyBaseUserTable, Model):
    username: Mapped[str] = mapped_column(
        String(length=1024), unique=True
    )
    first_name: Mapped[str] = mapped_column(
        String, nullable=True
    )
    last_name: Mapped[str] = mapped_column(
        String, nullable=True
    )
    phone: Mapped[str] = mapped_column(
        String, nullable=False, unique=True
    )


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, UserORM)
