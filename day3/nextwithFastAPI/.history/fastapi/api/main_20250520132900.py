from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.add_middleware(
    CORSMiddleware,
    allow
)

@app.get("/")
async def root():   
    return {"message": "Hello World"}

