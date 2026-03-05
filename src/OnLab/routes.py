from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from urllib.parse import unquote
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

@router.get("/hello")
async def hello():
    """Check gigachat status"""
    raw = [ai.invoke("Поприветствуй пользователя в научном стиле")]
    return AIResponse(content=raw)

@router.get("/entities", response_model=AIResponse)
async def get_entities(prompt: str):
    """AI Query"""
    raw = ai.invoke(unquote(prompt))
    res = pr.preprocess(raw)
    entities = res.get("entities", None)

    if not entities:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=entities)

@router.get("/stages", response_model=AIResponse)
async def get_stages(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    stages = res.get('stages', None)

    if not stages:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=stages)

@router.get("/transitions", response_model=AIResponse)
async def get_transitions(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    transitions = res.get('transitions', None)

    if not transitions:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=transitions)

@router.get("/params", response_model=AIResponse)
async def get_params(prompt: str):
    """AI Query"""
    raw = ai.invoke(prompt)
    res = pr.preprocess(raw)
    params = res.get('stages_params', None)

    if not params:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=params)
