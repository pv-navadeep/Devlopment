from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .database import SessionLocal
from .models import User
from fastapi.secur
from passlib.context import CryptContext
