from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from OnLab.gigachat import GigaEngine
from OnLab.preprocessor import Preprocessor


router = APIRouter()
ai = GigaEngine()
pr = Preprocessor()

class AIResponse(BaseModel):
    """Response template"""
    content: list | dict

class AIRequest(BaseModel):
    """Response template"""
    prompt: str

@router.get("/status")
async def status_check():
    """Check server status"""
    return {"status": "ok"}

@router.get("/gigachat")
async def hello():
    """Check gigachat status"""
    raw = [ai.invoke("Тестовое сообщение, чтобы проверить, что API работает!")]
    return AIResponse(content=raw)

@router.post("/entities", response_model=AIResponse)
async def get_entities(request: AIRequest):
    """AI Query"""
    raw = ai.invoke(request.prompt)
    res = pr.preprocess(raw)
    entities = res.get("entities", None)

    if not entities:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=entities)

@router.post("/stages", response_model=AIResponse)
async def get_stages(request: AIRequest):
    """AI Query"""
    raw = ai.invoke(request.prompt)
    res = pr.preprocess(raw)
    stages = res.get('stages', None)

    if not stages:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=stages)

@router.post("/transitions", response_model=AIResponse)
async def get_transitions(request: AIRequest):
    """AI Query"""
    raw = ai.invoke(request.prompt)
    res = pr.preprocess(raw)
    transitions = res.get('transitions', None)

    if not transitions:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=transitions)

@router.post("/params", response_model=AIResponse)
async def get_params(request: AIRequest):
    """AI Query"""
    raw = ai.invoke(request.prompt)
    res = pr.preprocess(raw)
    params = res.get('stages_params', None)

    if not params:
        raise HTTPException(status_code=500, detail="Error in JSON!")

    return AIResponse(content=params)
