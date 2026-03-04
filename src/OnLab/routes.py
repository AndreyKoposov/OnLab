from fastapi import APIRouter
from OnLab.gigachat import GigaEngine
from OnLab.models import AIPrompt, AIResponse
from OnLab.logger import LogManager


router = APIRouter()
ai = GigaEngine()


@router.get("/status")
async def health_check():
    """Check server status"""
    return {"status": "ok"}

@router.get("/entities", response_model=AIResponse)
async def get_entities(prompt: AIPrompt):
    """AI Query"""
    res = ai.invoke(prompt.text)

    LogManager.info(res)
    entities = res['entities']

    return AIResponse(content=entities)

@router.get("/stages", response_model=AIResponse)
async def get_stages(prompt: AIPrompt):
    """AI Query"""
    res = ai.invoke(prompt.text)

    LogManager.info(res)
    stages = res['stages']

    return AIResponse(content=stages)

@router.get("/transitions", response_model=AIResponse)
async def get_transitions(prompt: AIPrompt):
    """AI Query"""
    res = ai.invoke(prompt.text)

    LogManager.info(res)
    transitions = res['transitions']

    return AIResponse(content=transitions)
