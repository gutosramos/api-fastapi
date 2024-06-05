# migration.py
from sqlalchemy import create_engine
from app.models import Base
from app.database import SQLALCHEMY_DATABASE_URL

# Criar o engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Dropar todas as tabelas
Base.metadata.drop_all(bind=engine)

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)
