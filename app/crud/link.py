from sqlalchemy.orm import Session
from typing import List
from app.models.link import Link as LinkModel
from app.schemas import link as link_schemas
from datetime import datetime


def get_link(db: Session, link_id: int) -> LinkModel:
    return db.query(LinkModel).filter(LinkModel.id == link_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 20) -> List[LinkModel]:
    return db.query(LinkModel).offset(skip).limit(limit).all()

from sqlalchemy.orm import Session
from app.models.link import Link as LinkModel
from app.schemas import link as link_schemas
from datetime import datetime

def create_link(db: Session, link: link_schemas.LinkCreate) -> LinkModel:
    current_datetime = datetime.now()  # Obtenha a data e hora atuais
    db_link = LinkModel(
        descricao=link.descricao,
        link=link.link,
        created_at=current_datetime  # Defina a data de criação como a data e hora atuais
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link



def update_link(db: Session, link_id: int, link: link_schemas.LinkCreate) -> LinkModel:
    db_link = db.query(LinkModel).filter(LinkModel.id == link_id).first()
    if db_link is None:
        return None
    for attr, value in link.dict().items():
        setattr(db_link, attr, value)
    db_link.updated_at = datetime.now()
    db.commit()
    db.refresh(db_link)
    return db_link

def delete_link(db: Session, link_id: int) -> link_schemas.Link:
    db_link = db.query(LinkModel).filter(LinkModel.id == link_id).first()
    if db_link:
        db_link.deleted_at = datetime.now()
        db.commit()
        return db_link
    else:
        return None
