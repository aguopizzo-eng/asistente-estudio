from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlmodel import Session, select

from app.database import get_session
from app.models import Materia
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
