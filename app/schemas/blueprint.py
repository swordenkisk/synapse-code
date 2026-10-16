from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ArrayLayer(BaseModel):
    """The Array: Linear decomposition of requirements."""
    requirements: List[str] = Field(..., description="List of atomic functional requirements.")
    constraints: List[str] = Field(..., description="Technical or business constraints.")

class LatticeLayer(BaseModel):
    """The Lattice: Mapping inter-dependencies and relationships."""
    dependency_graph: List[Dict[str, str]] = Field(..., description="Mappings of Module A -> depends on -> Module B.")
    data_flow: str = Field(..., description="Description of how data moves through the system.")

class TensorLayer(BaseModel):
    """The Tensor: Multi-dimensional trade-off analysis."""
    scalability_score: int = Field(..., ge=1, le=10)
    maintainability_score: int = Field(..., ge=1, le=10)
    complexity_analysis: str = Field(..., description="Analysis of the most difficult technical hurdles.")

class GridLayer(BaseModel):
    """The Grid: The final English blueprint."""
    architecture_pattern: str = Field(..., description="e.g., Clean Architecture, Hexagonal, MVC.")
    file_structure: List[str] = Field(..., description="The complete proposed directory tree.")
    api_definitions: List[str] = Field(..., description="Detailed English descriptions of all endpoints/functions.")

class FinalCode(BaseModel):
    """The Operator Output: The actual IT implementation."""
    files: List[Dict[str, str]] = Field(..., description="List of objects containing 'path' and 'content'.")
