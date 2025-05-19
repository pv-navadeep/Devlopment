from fastapi import FastAPI
from src.books.routes import book_router
from fastapi.middleware.cors import CORSMiddleware
from src.db.main import Base, engine, UserBase, user_engine
from src.db import models
from src.db.user_routes import user_router

version = "v1"
app = FastAPI(
    title="Book API",
    description="API for managing books",
    version=version,
)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    UserBase.metadata.create_all(bind=user_engine)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
app.include_router(user_router, prefix=f"/api/{version}", tags=["users"])





























