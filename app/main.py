from fastapi import FastAPI, HTTPException
from app.cognitive.layers import SynapseBrain
from app.cognitive.operator import SynapseOperator
from pydantic import BaseModel

app = FastAPI(title="Synapse-Code AI Assistant")
brain = SynapseBrain()
operator = SynapseOperator()

class ProjectRequest(BaseModel):
    goal: str

@app.post("/build")
async def build_project(request: ProjectRequest):
    try:
        # Phase 1: Thinking (The Brain)
        blueprint_data = brain.process_blueprint(request.goal)
        
        # Phase 2: Execution (The Operator)
        grid_json = blueprint_data["grid"].model_dump_json()
        code_output = operator.generate_code(grid_json)
        
        return {
            "blueprint": blueprint_data,
            "code": code_output
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
