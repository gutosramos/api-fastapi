from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.get("/")
def root():
    return {"message": "up & running"}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/users", response_model=schemas.UserResponse, status_code=201)
async def create_user(payload: schemas.UserCreate,
                      db: AsyncSession = Depends(get_db)):
    user = models.User(name=payload.name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


@router.get("/users", response_model=List[schemas.UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    return result.scalars().all()
