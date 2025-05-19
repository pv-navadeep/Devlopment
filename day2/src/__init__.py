from fastapi import FastAPI
from src.books.routes import book_router
from fastapi.middleware.cors import CORSMiddleware

version = "v1"
app = FastAPI(
    title="Book API",
    description="API for managing books",
    version=version,
)


app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])





























