from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, index=True)
    link = Column(String, unique=True, index=True)
    
    created_at = Column(DateTime, default=func.now())  # Defina o valor padrão para created_at
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
