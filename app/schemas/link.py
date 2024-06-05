from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LinkBase(BaseModel):
    descricao: str
    link: str

class LinkCreate(LinkBase):
    pass

class Link(LinkBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        from_attributes = True  # Atualização para Pydantic V2
