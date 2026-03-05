from os import getenv
from typing import Literal
from pathlib import Path
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ROOT = Path.cwd()

class Settings(BaseSettings):
    """Загрузка переменных среды"""
    # AI
    AI_PROVIDER: Literal["gigachat", "yandexgpt"] = "gigachat"
    AI_MODEL: str = "GigaChat"
    AI_API_KEY: SecretStr = SecretStr('')
    AI_TEMP: float = Field(default=0.0, ge=0.0, le=1.0)

    # DEBUG
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=ROOT/".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )

    @property
    def get_model(self):
        "GET MODEL"
        if self.DEBUG:
            return self.AI_MODEL
        return getenv("AI_MODEL")

    @property
    def get_api_key(self):
        "GET MODEL"
        if self.DEBUG:
            return self.AI_API_KEY.get_secret_value()
        return getenv("AI_API_KEY")

    @property
    def get_temp(self):
        "GET MODEL"
        if self.DEBUG:
            return self.AI_TEMP
        return getenv("AI_TEMP")

ENV = Settings()
