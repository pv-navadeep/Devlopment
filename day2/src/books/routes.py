from fastapi import Depends, APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from src.books.schema import BookCreateModel
from src.db.models import Book
from src.db.session import get_db
from typing import List

book_router = APIRouter()


@book_router.get("/", response_model=List[BookCreateModel])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookCreateModel)
def create_book(book: BookCreateModel, db: Session = Depends(get_db)):
    db_book = Book(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@book_router.get("/{book_id}", response_model=BookCreateModel)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@book_router.patch("/{book_id}", response_model=BookCreateModel)
def update_book(book_id: int, book: BookCreateModel, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.title = book.title
    db_book.author = book.author
    db.commit()
    db.refresh(db_book)
    return db_book


@book_router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted"}

