from fastapi import APIRouter
from OnLab.backend.ai.giga_engine import GigaEngine
from OnLab.backend.models.process import ProcessDescription
from OnLab.backend.models.responses import AnalysisResponse


router = APIRouter()
ai = GigaEngine()

@router.post("/analyze/text", response_model=AnalysisResponse)
async def analyze_process_text(description: ProcessDescription):
    return AnalysisResponse(
            success=True,
            ontology=f"{description.text}",
            graph_data=["State1", "State2"],
            bifurcation_points=["if x then y", "if z then a"],
            message="Анализ выполнен успешно"
        )
