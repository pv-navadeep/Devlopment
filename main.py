from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

items = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id in items:
        return {"item_id": item_id, "value": items[item_id]}
    return JSONResponse(status_code=404, content={"error": "Item not found"})


@app.post("/items/")
async def create_item(request: Request):
    data = await request.json()
    item_id = data.get("item_id")
    value = data.get("value")
    if item_id is None or value is None:
        return JSONResponse(status_code=400, content={"error": "item_id and value required"})
    items[item_id] = value
    return {"item_id": item_id, "value": value}


@app.get("/items/")
def list_items():
    return [{"item_id": k, "value": v} for k, v in items.items()]

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id in items:
        del items[item_id]
        return {"message": "Item deleted"}
    return JSONResponse(status_code=404, content={"error": "Item not found"})       

@app.get("/")
def serve_frontend():
    frontend_path = os.path.join(os.path.dirname(__file__), "index.html")
    return FileResponse(frontend_path)