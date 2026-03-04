"""langchain_gigachat, langchain_core"""
from langchain_gigachat import GigaChat
from langchain_core.messages import AIMessage
from OnLab.logger import LogManager
from OnLab.config import ENV
from OnLab.ai_tools import TOOLS


class GigaEngine():
    """Класс для работы с gigachat api"""
    def __init__(self) -> None:
        giga = GigaChat(
            credentials=ENV.AI_API_KEY.get_secret_value(),
            model=ENV.AI_MODEL,
            verify_ssl_certs=False,
            temperature=ENV.AI_TEMP,
            scope="GIGACHAT_API_PERS",
            timeout=240
        )

        self.llm = giga.bind_tools(TOOLS)

        self.system_prompt = """Ты - ассистент по анализу сложных процессов.
        Ты помогаешь пользователю анализировать и модифицировать онтологические модели.
        Всегда используй инструменты (tools) для выполнения запросов."""

    def invoke(self, query: str) -> dict:
        """Делает обычный запрос"""
        res = self.llm.invoke(query)

        if isinstance(res, AIMessage):
            return res.tool_calls[0]['args']
        return {}

    def invoke_json(self, query: str) -> dict:
        """Делает запрос на получение json данных"""
        res = self.llm.invoke(query)
        LogManager.info(res)
        if isinstance(res, AIMessage):
            return res.tool_calls[0]['args']
        return {}
