from fastapi import FastAPI
from fastapi import HTTPException

app = FastAPI()

items = {1: 0, 2: 1, 3: 4}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/status")
async def read_root():
    return {"status": "ok"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item_quantity = items.get(item_id)
    if item_quantity is None:
        raise HTTPException(status_code=404, detail="item not found.")

    return {"item_id": item_id, "q": item_quantity}
