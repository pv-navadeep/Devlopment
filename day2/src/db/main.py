from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.settings import settings

# Main database
engine = create_engine(settings.DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Additional user database
USER_DATABASE_URL = "sqlite:///./user.db"
user_engine = create_engine(USER_DATABASE_URL)
UserBase = declarative_base()
UserSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=user_engine)

