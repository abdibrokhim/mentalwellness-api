
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from gpt import gen_title, conclude

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def read_root():
    return {"message": "Hello World"}

@app.post("/api/gpt4o")
def gpt(request_body: dict):
    messages = request_body.get("messages", "")
    return conclude(messages)

@app.post("/api/gpt4o/title")
def gpt_title(request_body: dict):
    messages = request_body.get("messages", "")
    return gen_title(messages)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)