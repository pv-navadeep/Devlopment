from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.settings import settings
from src.db.models import Book

engine = create_engine(settings.DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)