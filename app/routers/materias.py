from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select

from app.database import get_session
from app.models import Materia, Tema
from app.templating import templates

router = APIRouter()


@router.get("/materias")
def listar_materias(request: Request, session: Session = Depends(get_session)):
    materias = session.exec(select(Materia).order_by(Materia.nombre)).all()
    return templates.TemplateResponse(request, "materias.html", {"materias": materias})


@router.post("/materias")
def crear_materia(nombre: str = Form(...), session: Session = Depends(get_session)):
    nombre = nombre.strip()
    if nombre:
        session.add(Materia(nombre=nombre))
        session.commit()
    return RedirectResponse("/materias", status_code=303)


@router.get("/materias/{materia_id}")
def ver_materia(materia_id: int, request: Request, session: Session = Depends(get_session)):
    materia = session.get(Materia, materia_id)
    if materia is None:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    temas = session.exec(
        select(Tema).where(Tema.materia_id == materia_id).order_by(Tema.nombre)
    ).all()
    return templates.TemplateResponse(
        request, "materia_detalle.html", {"materia": materia, "temas": temas}
    )
