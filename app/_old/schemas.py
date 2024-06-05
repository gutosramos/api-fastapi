from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Atualização para Pydantic V2

class LinkBase(BaseModel):
    descricao: str
    link: str

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True  # Atualização para Pydantic V2
