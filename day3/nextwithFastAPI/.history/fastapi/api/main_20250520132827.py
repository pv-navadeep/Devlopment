from fastapi import FastAPI
from fastapi.middleware.cors import CRS

app = FastAPI()

@app.add_middleware

@app.get("/")
async def root():   
    return {"message": "Hello World"}

