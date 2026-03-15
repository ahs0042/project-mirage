from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mirage Auth Service")


class LoginRequest(BaseModel):
    username: str
    password: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/login")
def login(payload: LoginRequest):
    if payload.username == "admin":
        return {
            "access_token": "mirage-admin-token",
            "role": "admin"
        }

    return {
        "access_token": "mirage-user-token",
        "role": "user"
    }


@app.get("/validate")
def validate(token: str):
    if token in ["mirage-admin-token", "mirage-user-token"]:
        return {"valid": True}
    return {"valid": False}
