from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from app import models  # noqa: F401  (hace que Python conozca las tablas)
from app.database import crear_tablas
from app.routers import materias, temas
from app.templating import templates


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="Asistente de Estudio", lifespan=lifespan)
app.include_router(materias.router)
app.include_router(temas.router)


@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(request, "inicio.html")
