from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI(title="Mirage API Gateway")

AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL", "http://auth-service:8001")
CATALOG_SERVICE_URL = os.getenv("CATALOG_SERVICE_URL", "http://catalog-service:8002")
RECOMMENDATION_SERVICE_URL = os.getenv("RECOMMENDATION_SERVICE_URL", "http://recommendation-service:8003")


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/catalog")
def catalog():
    response = requests.get(f"{CATALOG_SERVICE_URL}/catalog")
    return response.json()


@app.get("/api/featured")
def featured():
    response = requests.get(f"{CATALOG_SERVICE_URL}/featured")
    return response.json()


@app.get("/api/recommended")
def recommended():
    response = requests.get(f"{RECOMMENDATION_SERVICE_URL}/recommended")
    return response.json()


@app.get("/api/trending")
def trending():
    response = requests.get(f"{RECOMMENDATION_SERVICE_URL}/trending")
    return response.json()


@app.post("/api/login")
def login(payload: LoginRequest):
    response = requests.post(
        f"{AUTH_SERVICE_URL}/login",
        json=payload.dict()
    )
    return response.json()
