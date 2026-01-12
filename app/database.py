import os
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://api_user:api_pass@db:5432/api_db"
)

engine = create_async_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
