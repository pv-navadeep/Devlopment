from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated
from pydantic import BaseModel
from jose import JWTErrorfrom
from dotenv import load_dotenv
import os
from api.models import User
from api.database import SessionLocal
from api.deps import get_db, oauth2_scheme
from api.deps import db_dependency,bcrypt_context

load_