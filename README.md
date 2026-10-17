# Synapse-Code 

Synapse-Code is a Senior AI Project Architect that replaces "guessing" with a scientific, layered cognitive process.

## The Cognitive Pipeline
The system processes every request through these dimensions:
1. **The Array**: Breaks the goal into linear, atomic requirements.
2. **The Lattice**: Maps how components relate and depend on one another.
3. **The Tensor**: Evaluates the project's "tension" (Scalability vs. Speed vs. Cost).
4. **The Grid**: Finalizes a strict English-language technical specification.
5. **The Operator**: Transforms the Grid into a full IT repository.

## Prerequisites
- Python 3.10+
- OpenAI API Key (GPT-4o recommended for structured output)

## Installation
```bash
chmod +x setup.sh
./setup.sh
source venv/bin/activate
Usage
Start the API:
bash


uvicorn app.main:app --reload
Send a POST request to /build:
json


{
  "goal": "Create a high-performance pricing calculator for a SaaS agency that handles dynamic currency conversion and tiered discounts."
}
Testing
bash


pytest tests/test\_architect.py



### Core Functionality Test: `tests/test_architect.py`
```python
import pytest
from app.cognitive.layers import SynapseBrain

def test_brain_pipeline():
    # Requires valid .env
    brain = SynapseBrain()
    goal = "A simple Todo list API"
    result = brain.process_blueprint(goal)
    
    assert "grid" in result
    assert "array" in result
    assert len(result["grid"].file_structure) > 0
