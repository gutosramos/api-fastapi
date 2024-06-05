from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from datetime import datetime
from typing import List

def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    return db.query(User).filter(User.deleted_at == None).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        name=user.name,
        email=user.email,
        password=fake_hashed_password,
        created_at=datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserCreate) -> User:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    for attr, value in user.dict().items():
        setattr(db_user, attr, value)
    db_user.updated_at = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int) -> User:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.deleted_at = datetime.now()
        db.commit()
    return db_user
