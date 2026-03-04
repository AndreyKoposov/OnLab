"""langchain_gigachat, langchain_core"""
from langchain_gigachat import GigaChat
from OnLab.logger import Logger
from OnLab.config import ENV


class GigaEngine():
    """Класс для работы с gigachat api"""
    def __init__(self) -> None:
        self.giga = GigaChat(
            credentials=ENV.AI_API_KEY.get_secret_value(),
            model=ENV.AI_MODEL,
            verify_ssl_certs=False,
            temperature=ENV.AI_TEMP,
            scope="GIGACHAT_API_PERS",
            timeout=240
        )

    def invoke(self, query: str) -> str:
        """Делает запрос на получение json данных"""
        res = self.giga.invoke(query).content

        if isinstance(res, str):
            Logger.info(f"AI response:\n{res}")
            return res

        Logger.error(f"Bad AI answer:\n{res}")
        return ""
