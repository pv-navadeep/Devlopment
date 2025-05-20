from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine
from sqlalchemy.engine import Connection

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_Engine()