from fastapi import FastAPI

app = FastAPI(title="Mirage Catalog Service")

catalog = [
    {
        "id": 1,
        "title": "Edge of Tomorrow",
        "genre": "Sci-Fi",
        "year": 2014,
        "rating": 8.0
    },
    {
        "id": 2,
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "year": 2014,
        "rating": 8.6
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "genre": "Action",
        "year": 2008,
        "rating": 9.0
    }
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/catalog")
def get_catalog():
    return catalog


@app.get("/catalog/{item_id}")
def get_catalog_item(item_id: int):
    for item in catalog:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.get("/featured")
def featured():
    return [catalog[0], catalog[1]]
