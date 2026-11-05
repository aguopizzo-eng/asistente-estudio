from typing import Annotated, Optional

from pydantic import BaseModel, StringConstraints, ValidationError

# Texto que no puede quedar vacío (se le quitan los espacios de los costados).
Obligatorio = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]
# Texto que puede quedar vacío.
Opcional = Annotated[str, StringConstraints(strip_whitespace=True)]


class CamposCornell(BaseModel):
    preguntas_clave: Obligatorio
    notas: Obligatorio
    resumen: Obligatorio


class CamposCamino(BaseModel):
    enunciado: Obligatorio
    primera_intuicion: Opcional = ""
    camino: Opcional = ""
    donde_me_trabe: Opcional = ""
    idea_clave: Obligatorio
    conexiones: Opcional = ""


TIPOS = {
    "cornell": CamposCornell,
    "camino": CamposCamino,
}


def validar_campos(tipo: str, datos: dict) -> tuple[Optional[dict], dict]:
    """Devuelve (campos_limpios, errores). Si todo está bien, errores es {}."""
    modelo = TIPOS.get(tipo)
    if modelo is None:
        return None, {"tipo": "Tipo de apunte desconocido"}

    try:
        return modelo(**datos).model_dump(), {}
    except ValidationError as e:
        errores = {}
        for error in e.errors():
            campo = str(error["loc"][0])
            if error["type"] in ("missing", "string_too_short"):
                errores[campo] = "Este campo es obligatorio"
            else:
                errores[campo] = "Valor no válido"
        return None, errores
