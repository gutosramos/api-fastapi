from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
import os

from database import AsyncSessionLocal
import models
import schemas

app = FastAPI(title="FastAPI Dev Stack")


# =========================
# Database dependency
# =========================
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


# =========================
# Healthcheck
# =========================
@app.get("/health")
async def health():
    return {"status": "ok"}


# =========================
# Create user
# =========================
@app.post(
    "/users",
    response_model=schemas.UserResponse,
    status_code=201,
)
async def create_user(
    payload: schemas.UserCreate,
    db: AsyncSession = Depends(get_db),
):
    user = models.User(name=payload.name)

    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user


# =========================
# List users
# =========================
@app.get(
    "/users",
    response_model=List[schemas.UserResponse],
)
async def list_users(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users


# =========================
# Root
# =========================
@app.get("/")
async def root():
    return {
        "status": "ok",
        "env": os.getenv("ENVIRONMENT"),
        "db_host": os.getenv("POSTGRES_HOST"),
    }
