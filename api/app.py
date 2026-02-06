from fastapi import FastAPI
from main import NexusOrchestrator  # Import the orchestrator we just built

app = FastAPI(title="Nexus Agent API")
nexus = NexusOrchestrator()

@app.get("/query")
async def chat(q: str):
    response = nexus.handle_query(q)
    return {"status": "success", "response": response}