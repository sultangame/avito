from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from dotenv import load_dotenv
import os


load_dotenv()

async_url = os.environ.get("URL")
async_engine = create_async_engine(url=async_url)
async_session_maker = async_sessionmaker(bind=async_engine)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
