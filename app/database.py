import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from .models import Base

# monta a URL a partir das vars que você já declarou no compose
user = os.getenv("DB_USER", "api_user")
pwd  = os.getenv("DB_PASS", "api_pass")
host = os.getenv("DB_HOST", "db")
port = os.getenv("DB_PORT", "5432")
db   = os.getenv("DB_NAME", "api_db")

DATABASE_URL = f"postgresql+asyncpg://{user}:{pwd}@{host}:{port}/{db}"

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
