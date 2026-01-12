# from fastapi import FastAPI
# from app.database import create_db_and_tables
# from app.routers import items

# app = FastAPI(title="API-FastAPI", version="0.1.0")

# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()

# app.include_router(items.router, prefix="/items", tags=["items"])

# @app.get("/")
# def root():
#     return {"message": "up & running"}
# # =========================
# # Database dependency
# # =========================
# async def get_db() -> AsyncSession:
#     async with AsyncSessionLocal() as session:
#         yield session


# # =========================
# # Healthcheck
# # =========================
# @app.get("/health")
# async def health():
#     return {"status": "ok"}


# # =========================
# # Create user
# # =========================
# @app.post(
#     "/users",
#     response_model=schemas.UserResponse,
#     status_code=201,
# )
# async def create_user(
#     payload: schemas.UserCreate,
#     db: AsyncSession = Depends(get_db),
# ):
#     user = models.User(name=payload.name)

#     db.add(user)
#     await db.commit()
#     await db.refresh(user)

#     return user


# # =========================
# # List users
# # =========================
# @app.get(
#     "/users",
#     response_model=List[schemas.UserResponse],
# )
# async def list_users(
#     db: AsyncSession = Depends(get_db),
# ):
#     result = await db.execute(select(models.User))
#     users = result.scalars().all()
#     return users




from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers.items import router  #  👈 import direto

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()

app.include_router(router, prefix="/items", tags=["items"])


@app.get("/health")
async def health():
    return {"status": "ok"}