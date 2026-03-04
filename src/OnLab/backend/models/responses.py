from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    success: bool
    ontology: str
    graph_data: list
    bifurcation_points: list
    message: str