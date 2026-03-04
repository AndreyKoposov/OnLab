from pydantic import BaseModel


class AIPrompt(BaseModel):
    text: str

class AIResponse(BaseModel):
    content: list