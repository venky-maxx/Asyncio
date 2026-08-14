from fastapi import FastAPI
import uvicorn

app = FastAPI(title ="my first api call")

@app.get("/first_endpoint")
async def first_endpoint():
    return {"response" : "Hello_world"}

if __name__ == "__main__":
    uvicorn.run(
        "main_fast_api:app",
        host = "0.0.0.0",
        port = 8000,
        reload = True
    )