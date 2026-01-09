from pydantic import BaseModel, ConfigDict


# =========================
# Base
# =========================
class UserBase(BaseModel):
    name: str


# =========================
# Create
# =========================
class UserCreate(UserBase):
    pass


# =========================
# Response
# =========================
class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
