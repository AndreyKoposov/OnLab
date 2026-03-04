from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from OnLab.routes import router as api_router


app = FastAPI(title="Ontology Lab")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")


"""
Фотолитография — метод получения рисунка на поверхности материала. На подложку наносится фоторезист, который засвечивается через фотошаблон, проявляется, а затем используется для травления или напыления. Фотолитография начинается с нанесения фоторезиста на подложку. Затем происходит засвечивание через фотошаблон, проявление и использование для травления или напыления.
"""