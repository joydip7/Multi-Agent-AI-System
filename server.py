from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from main import MultiAgentSystem
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Initialize your multi-agent system
system = MultiAgentSystem()

# Serve frontend static files
app.mount("/static", StaticFiles(directory="static"), name="static")

class GoalRequest(BaseModel):
    goal: str


# Serve frontend at root URL
@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")


# Main AI endpoint
@app.post("/generate")
def generate_plan(request: GoalRequest):
    result = system.run(request.goal)

    return {
        "strategy": result["strategy"],
        "tasks": result["tasks"],
        "final_output": result["final_output"]
    }