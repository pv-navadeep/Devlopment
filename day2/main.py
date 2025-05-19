from fastapi import FastAPI , Header
from  typing import Optional 
from pydantic import BaseModel
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

class BookCreateModel(BaseModel):
    title: str
    author: str
@app.post("/create_books")
async def create_book(book: BookCreateModel):
    return { "message" : f"Book '{book.title}' by {book.author} has been created." } 

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

books_db = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"},
]

@app.get("/books")
async def get_books():
    return books_db

