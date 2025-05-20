from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    pass
    return {"message": "Hello World"}