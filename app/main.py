from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, get_db
from app.models.user import User as UserModel
from app.models.link import Link as LinkModel
from app.schemas import user as user_schemas, link as link_schemas
from app.crud import user as user_crud, link as link_crud
from typing import List
from app.database import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Middleware para forçar JSON nas respostas
@app.middleware("http")
async def force_json(request: Request, call_next):
    response = await call_next(request)
    if not response.headers.get("Content-Type"):
        response.headers["Content-Type"] = "application/json"
    return response

# Rotas de Usuários
@app.get("/users", response_model=List[user_schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)

@app.put("/users/{user_id}", response_model=user_schemas.User)
def update_user(user_id: int, user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update_user(db=db, user_id=user_id, user=user)

@app.delete("/users/{user_id}", response_model=user_schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db=db, user_id=user_id)
    return db_user

# Rotas de Links
@app.get("/links", response_model=List[link_schemas.Link])
def read_links(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    links = link_crud.get_links(db, skip=skip, limit=limit)
    return links

@app.get("/links/{link_id}", response_model=link_schemas.Link)
def read_link(link_id: int, db: Session = Depends(get_db)):
    db_link = link_crud.get_link(db, link_id=link_id)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return db_link

@app.post("/links", response_model=link_schemas.Link)
def create_link(link: link_schemas.LinkCreate, db: Session = Depends(get_db)):
    return link_crud.create_link(db=db, link=link)

@app.put("/links/{link_id}", response_model=link_schemas.Link)
def update_link(link_id: int, link: link_schemas.LinkCreate, db: Session = Depends(get_db)):
    db_link = link_crud.get_link(db, link_id=link_id)
    if db_link is None:
        raise HTTPException(status_code=404, detail="Link not found")
    return link_crud.update_link(db=db, link_id=link_id, link=link)

@app.delete("/links/{link_id}", response_model=link_schemas.Link)
def delete_link(link_id: int, db: Session = Depends(get_db)):
    db_link = link_crud.get_link(db, link_id=link_id)
    if db_link is None:
        raise HTTPException(status_code=404,detail="Link not found")
    link_crud.delete_link(db=db, link_id=link_id)
    return db_link

@app.get("/hello")
def read_hello():
    return {"hello": "world"}
