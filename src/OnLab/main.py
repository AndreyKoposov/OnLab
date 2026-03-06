from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from OnLab.routes import router as api_router
from OnLab.logger import Logger
from OnLab.config import ENV


if ENV.DEBUG:
    print("STARTED IN DEBUG FORMAT")
    Logger.start()
else:
    print("STARTED IN PRODUCTION FORMAT")

app = FastAPI(title="Ontology Lab")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")

@app.head("/ping")
async def ping_head():
    """HEAD запросы"""
    return Response(status_code=200)

Logger.info("started")



#Фотолитография — метод получения рисунка на поверхности материала.
#На подложку наносится фоторезист, который засвечивается через фотошаблон,
#проявляется, а затем используется для травления или напыления. Фотолитография
#начинается с нанесения фоторезиста на подложку. Затем происходит засвечивание
#через фотошаблон, проявление и использование для травления или напыления.
