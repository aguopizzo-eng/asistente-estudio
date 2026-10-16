from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field


class Materia(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    creado_en: datetime = Field(default_factory=datetime.now)


class Tema(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    materia_id: int = Field(foreign_key="materia.id")
    nombre: str
    creado_en: datetime = Field(default_factory=datetime.now)
