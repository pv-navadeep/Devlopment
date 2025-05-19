from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db.models import User
from src.db.main import UserSessionLocal
from src.db.user_schema import UserCreateModel, UserResponseModel
from typing import List

user_router = APIRouter()

@user_router.post("/register", response_model=UserResponseModel, status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreateModel):
    db = UserSessionLocal()
    try:
        db_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username or email already registered")
        new_user = User(username=user.username, email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    finally:
        db.close()

@user_router.get("/users", response_model=List[UserResponseModel])
def list_users():
    db = UserSessionLocal()
    try:
        return db.query(User).all()
    finally:
        db.close()
