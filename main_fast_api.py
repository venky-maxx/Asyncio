from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title ="my first api call")

class User(BaseModel):
    username : str
    email:str
    age:int

@app.get("/first_endpoint")
async def first_endpoint():
    return {"response" : "Hello_world"}

@app.post("/user/registration")
async def user_register(user_details:User):
    msg = f"{user_details.username} is registered successfully...!"
    return msg 

if __name__ == "__main__":
    uvicorn.run(
        "main_fast_api:app",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )