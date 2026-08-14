from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import logging, json, time

app = FastAPI(title ="my first api call")


class User(BaseModel):
    username : str
    email:str
    age:int

class JsonLogger(logging.Formatter):
    def format(self, record):
        log_record = {
            "level": record.levelname,
            "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created)),
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


log = logging.getLogger("my_sample_logging")
log.setLevel(logging.INFO)
h = logging.StreamHandler();h.setFormatter(JsonLogger())
z = logging.FileHandler('web.log');z.setFormatter(JsonLogger())
log.addHandler(h)
log.addHandler(z)
log.propagate = False 


@app.get("/first_endpoint")
async def first_endpoint():
    return {"response" : "Hello_world"}

@app.post("/user/registration")
async def user_register(user_details:User):
    log.info(f"User details received {user_details}")
    msg = f"{user_details.username} is registered successfully...!"
    return msg 

if __name__ == "__main__":
    uvicorn.run(
        "main_fast_api:app",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )