from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import Session

from app.database import get_session
from app.models import Materia, Tema

router = APIRouter()


@router.post("/materias/{materia_id}/temas")
def crear_tema(
    materia_id: int,
    nombre: str = Form(...),
    session: Session = Depends(get_session),
):
    materia = session.get(Materia, materia_id)
    if materia is None:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    nombre = nombre.strip()
    if nombre:
        session.add(Tema(materia_id=materia_id, nombre=nombre))
        session.commit()
    return RedirectResponse(f"/materias/{materia_id}", status_code=303)
