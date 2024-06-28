
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gpt

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
def gemini(request_body: dict):
    messages = request_body.get("messages", "")
    return gpt.conclude(messages)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)