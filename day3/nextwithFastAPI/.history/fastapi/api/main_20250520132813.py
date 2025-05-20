from fastapi import FastAPI
from fastapi.exec.

app = FastAPI()

@app.add_middleware

@app.get("/")
async def root():   
    return {"message": "Hello World"}

