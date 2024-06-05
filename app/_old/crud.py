from sqlalchemy.orm import Session
from app import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(name=user.name, email=user.email, password=fake_hashed_password)  # Atualizado para usar `password`
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_links(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Link).offset(skip).limit(limit).all()

def get_link(db: Session, link_id: int):
    return db.query(models.Link).filter(models.Link.id == link_id).first()

def create_link(db: Session, link: schemas.LinkCreate):
    db_link = models.Link(**link.dict())
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link

def delete_link(db: Session, link_id: int):
    db.query(models.Link).filter(models.Link.id == link_id).delete()
    db.commit()

def update_link(db: Session, link_id: int, link: schemas.LinkCreate):
    db_link = db.query(models.Link).filter(models.Link.id == link_id).first()
    if db_link:
        db_link.descricao = link.descricao
        db_link.link = link.link
        db.commit()
        db.refresh(db_link)
    return db_link