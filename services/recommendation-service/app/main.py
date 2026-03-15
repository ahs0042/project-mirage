from fastapi import FastAPI

app = FastAPI(title="Mirage Recommendation Service")

recommended_items = [
    {"id": 101, "title": "Inception", "reason": "Because you watched Interstellar"},
    {"id": 102, "title": "The Matrix", "reason": "Trending in Sci-Fi"},
]

trending_items = [
    {"id": 201, "title": "Dune: Part Two", "rank": 1},
    {"id": 202, "title": "Severance", "rank": 2},
]

continue_watching_items = [
    {"id": 301, "title": "Stranger Things", "progress": "65%"},
    {"id": 302, "title": "The Bear", "progress": "40%"},
]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/recommended")
def recommended():
    return recommended_items


@app.get("/trending")
def trending():
    return trending_items


@app.get("/continue-watching")
def continue_watching():
    return continue_watching_items
