from fastapi import FastAPI

app = FastAPI()

@app.add_middleware

@app.get("/")
async def root():   
    return {"message": "Hello World"}

