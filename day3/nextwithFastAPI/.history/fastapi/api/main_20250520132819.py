from fastapi import FastAPI
from fastapi.middle

app = FastAPI()

@app.add_middleware

@app.get("/")
async def root():   
    return {"message": "Hello World"}

