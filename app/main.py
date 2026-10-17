from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from app import models  # noqa: F401  (hace que Python conozca las tablas)
from app.database import crear_tablas

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="Asistente de Estudio", lifespan=lifespan)


@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(request, "inicio.html")
