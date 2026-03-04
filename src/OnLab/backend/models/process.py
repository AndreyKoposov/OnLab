from pydantic import BaseModel
from typing import List, Dict, Optional, Any

class Parameter(BaseModel):
    name: str
    type: str  # "output", "control", "resource"
    unit: Optional[str] = None
    threshold: Optional[float] = None

class Stage(BaseModel):
    name: str
    description: Optional[str] = None
    parameters: List[Parameter] = []
    transitions_to: List[str] = []  # названия следующих этапов

class BifurcationPoint(BaseModel):
    stage: str
    condition: str
    threshold: Optional[float]
    effect: str
    severity: str  # "low", "medium", "high"

class ProcessOntology(BaseModel):
    name: str
    stages: List[Stage]
    bifurcation_points: List[BifurcationPoint] = []
    dependencies: Dict[str, List[str]] = {}  # связи параметров

class ProcessDescription(BaseModel):
    text: str
    format: str = "text"  # text, markdown, etc.