from fastapi import FastAPI
from pydantic import BaseModel
from main import MultiAgentSystem
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
system = MultiAgentSystem()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

class GoalRequest(BaseModel):
    goal: str

@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/generate")
def generate_plan(request: GoalRequest):
    result = system.run(request.goal)
    return {"output": result}
