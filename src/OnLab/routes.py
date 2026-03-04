from fastapi import APIRouter
from pydantic import BaseModel
from OnLab.gigachat import GigaEngine
from OnLab.preprocessor import Preprocessor


router = APIRouter()
ai = GigaEngine()
pr = Preprocessor()

class AIResponse(BaseModel):
    """Response template"""
    content: list

@router.get("/status")
async def status_check():
    """Check server status"""
    return {"status": "ok"}

@router.get("/entities", response_model=AIResponse)
async def get_entities(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    entities = res["entities"]

    return AIResponse(content=entities)

@router.get("/stages", response_model=AIResponse)
async def get_stages(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    stages = res['stages']

    return AIResponse(content=stages)

@router.get("/transitions", response_model=AIResponse)
async def get_transitions(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    transitions = res['transitions']

    return AIResponse(content=transitions)

@router.get("/params", response_model=AIResponse)
async def get_params(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    params = res['stages_params']

    return AIResponse(content=params)
