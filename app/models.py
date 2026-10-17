from datetime import datetime, timezone
from typing import Optional

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
