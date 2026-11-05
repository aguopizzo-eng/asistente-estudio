from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import JSON, Column
from sqlmodel import SQLModel, Field


def ahora() -> datetime:
    return datetime.now(timezone.utc)


class Materia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    creado_en: datetime = Field(default_factory=ahora)


class Tema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    materia_id: int = Field(foreign_key="materia.id")
    nombre: str
    creado_en: datetime = Field(default_factory=ahora)


class Apunte(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tema_id: int = Field(foreign_key="tema.id")
    tipo: str  # "cornell" o "camino" (más adelante "feynman")
    titulo: str
    campos: dict = Field(default_factory=dict, sa_column=Column(JSON))
    creado_en: datetime = Field(default_factory=ahora)
    actualizado_en: datetime = Field(default_factory=ahora)
