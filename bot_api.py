from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample user data
users = {
    "0901000001": "2070",
    "0901000002": "4321",
    "0901000003": "1111",
    "0901000004": "0000"
}

class LoginRequest(BaseModel):
    username: str
    pin: str

@app.post("/login")
def login(request: LoginRequest):
    if users.get(request.username) == request.pin:
        return {"status": "success"}
    return {"status": "failed"}
