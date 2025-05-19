from fastapi import APIRouter
from fastapi import FastAPI , Header,status
from fastapi.exceptions import HTTPException
from  typing import Optional
from src.books.schema import BookCreateModel
from typing import Dict, Any, List
from fastapi import Body
from src.books.book_Data import books_db

book_router = APIRouter()


@book_router.get("/")
async def get_books():
    return books_db

@book_router.post("/",status_code = status.HTTP_201_CREATED)
async def create_book(book :BookCreateModel):
    new_book = {
        "id" : len(books_db)+1,
        "title" : book.title,
        "author" : book.author
    }
    books_db.append(new_book)
    return new_book

@book_router.patch("/{book_id}")
async def update_book(book_id: int, book: Dict[str, Any] = Body(...)):
    for b in books_db:
        if b["id"] == book_id:
            if "title" in book:
                b["title"] = book["title"]
            if "author" in book:
                b["author"] = book["author"]
            return b
    return HTTPException(status_code=404, detail="Book not found")

@book_router.delete("/book_id")
async def delete_book(book_id : int):
    for b in books_db:
        if b["id"] == book_id :
            books_db.remove(b)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}  

@book_router.get("/{book_id}")
async def get_book(book_id: int):
    for b in books_db:
        if b["id"] == book_id:
            return b
    return HTTPException(status_code = 404 , detail= " Book not found")

