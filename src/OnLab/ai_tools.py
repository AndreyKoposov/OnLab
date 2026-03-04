"""import langchain, typing, json"""
from typing import Dict
import json
from langchain.tools import tool


@tool
def select_entities(entities: list[str]) -> str:
    """Превращает сущности процесса в элементы графа."""
    return "Основные сущности процесса:\n- " + "\n- ".join(entities)

@tool
def select_stages(stages: list[str]) -> str:
    """Превращает этапы процесса в элементы графа."""
    return "Основные этапы процесса:\n- " + "\n- ".join(stages)

@tool
def select_transitions(transitions: list[str]) -> str:
    """Превращает переходы процесса в элементы графа."""
    return "Переходы между этапами:\n- " + "\n- ".join(transitions)

@tool
def describe_params(stages_params: str) -> Dict:
    """
    Обрабатывает json с описанием параметров этапов процесса.
    
    Args:
        stages_params: json, содержащий этапы процесса и их параметры.
        
    Returns:
        Строковое представление обработанного JSON.
    """
    return json.loads(stages_params)

@tool
def analyze_params(params_weights: str) -> Dict:
    """
    Обрабатывает json с весами значимости параметров этапов процесса.
    
    Args:
        params_weights: json, содержащий веса параметров
        
    Returns:
        Строковое представление обработанного JSON.
    """
    return json.loads(params_weights)

TOOLS = [select_transitions, select_entities, select_stages, describe_params, analyze_params]