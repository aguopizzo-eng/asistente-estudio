from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import models  # noqa: F401  (hace que Python conozca las tablas)
from app.database import crear_tablas


@asynccontextmanager
async def lifespan(app: FastAPI):
    crear_tablas()
    yield


app = FastAPI(title="Asistente de Estudio", lifespan=lifespan)


@app.get("/")
def inicio():
    return {"mensaje": "Hola, asistente de estudio"}
