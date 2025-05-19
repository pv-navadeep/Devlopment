from fastapi import FastAPI , Header,status
from fastapi.exceptions import HTTPException
from  typing import Optional 
from pydantic import BaseModel
from typing import Dict, Any, List
from fastapi import Body


app = FastAPI()

@app.get("/")
async def root_page():
    return { "message" :  "Hello welcome to the FastAPI application" } 

@app.get("/greet/")
async def greet_user(name: str):
    return { "message" : f"Hello {name}, welcome to the FastAPI application" }

@app.get("/greet/{name}")
async def greet_user_path(name: Optional[str] = None, age: Optional[int] = 0):
    if age > 0:
        return { "message" : f"Hello {name}, welcome to the FastAPI application. You are {age} years old." }
    else: 
        return { "message" : f"Hello {name}, welcome to the FastAPI application. Your age is not provided." }   
    
@app.post("/greet/")
async def greet_user_post(name: str):
    return { "message" : f"Hello {name}, welcome to the FastAPI application. This is a POST request." }    


@app.get("/get_headers")
async def get_headers(user_agent: Optional[str] = None,
                      accept: Optional[str] = Header(None),
                      content_type: Optional[str] = Header(None),
                      x_custom_header: Optional[str] = Header(None),
                        
                      ):
    
    if user_agent:
        return { "message" : f"User-Agent: {user_agent}" }
    else:
        return { "message" : "No User-Agent provided." }

#crud operations


class BookCreateModel(BaseModel):
    title: str
    author: str


books_db = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

@app.get("/books")
async def get_books():
    return books_db

@app.post("/books",status_code = status.HTTP_201_CREATED)
async def create_book(book :BookCreateModel):
    new_book = {
        "id" : len(books_db)+1,
        "title" : book.title,
        "author" : book.author
    }
    books_db.append(new_book)
    return new_book

@app.patch("/book/{book_id}")
async def update_book(book_id: int, book: Dict[str, Any] = Body(...)):
    for b in books_db:
        if b["id"] == book_id:
            if "title" in book:
                b["title"] = book["title"]
            if "author" in book:
                b["author"] = book["author"]
            return b
    return {"message": "Book not found"}

@app.delete("/book/book_id")
async def delete_book(book_id : int):
    for b in books_db:
        if b["id"] == book_id :
            books_db.remove(b)
            return {"message": "Book deleted"}
    return {"message": "Book not found"}  

@app.get("/book/{book_id}")
async def get_book(book_id: int):
    for b in books_db:
        if b["id"] == book_id:
            return b
    return HTTPException(status_code = 404 , detail= " Book not found")



      

