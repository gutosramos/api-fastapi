from fastapi import APIRouter

router = APIRouter()

# @router.get("/")
# def read_items():
#     return {"ITEMS": "ok"}


@router.get("/")
def root():
    return {"message": "up & running"}


# =========================
# Healthcheck
# =========================
@router.get("/health")
async def health():
    return {"status": "ok"}


# =========================
# Create user
# =========================
@router.post(
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
@router.get(
    "/users",
    response_model=List[schemas.UserResponse],
)
async def list_users(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users
