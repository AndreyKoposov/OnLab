from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from OnLab.backend.api.routes import router as api_router
from OnLab.backend.models.responses import AnalysisResponse


app = FastAPI(title="Ontology Lab")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

app.mount("/static/", StaticFiles(directory="D:\\OnLab\\src\\OnLab\\frontend", html=True), name="frontend")
