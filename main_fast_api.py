from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import logging, json, time
from fastapi.responses import StreamingResponse
import asyncio

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

class Question(BaseModel):
    question : str

@app.post("/streaming")
async def streaming(question:Question):
    return StreamingResponse(
        stream_answer(question), 
        media_type ="text/plain"
    )

async def stream_answer(question:str):
    ans = """A big lion was sleeping peacefully under a tree in the green jungle. A tiny mouse ran across his paw by accident. The sudden movement woke the lion up.The angry lion caught the little mouse in his giant paw and opened his mouth to eat him. The scared mouse cried out, "Please, do not eat me! If you let me go, I will help you one day!"The lion laughed because the mouse was so small. How could a tiny creature ever help a strong lion? Still, the kind lion opened his paw and let the mouse run away.A few weeks later, hunters walked through the jungle. They caught the big lion in a strong rope net tied to a tree. The lion roared loudly, unable to break free.The little mouse heard the loud roar and ran over to help. Using his sharp teeth, the mouse chewed through the tough ropes quickly. Soon, the big lion was free again.The lion smiled at his tiny friend and learned a great truth: even the smallest friend can be a great help."""
    for word in ans.split(" "):
        yield word +" "
        await asyncio.sleep(0.1)



if __name__ == "__main__":
    uvicorn.run(
        "main_fast_api:app",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )