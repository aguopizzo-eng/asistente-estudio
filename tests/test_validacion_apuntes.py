from app.schemas import validar_campos


def test_cornell_valido():
    datos = {"preguntas_clave": "¿Qué es una pila?", "notas": "Estructura LIFO", "resumen": "Último en entrar, primero en salir"}
    campos, errores = validar_campos("cornell", datos)
    assert errores == {}
    assert campos["notas"] == "Estructura LIFO"


def test_cornell_sin_resumen_se_rechaza():
    datos = {"preguntas_clave": "¿Qué es una pila?", "notas": "Estructura LIFO"}
    campos, errores = validar_campos("cornell", datos)
    assert campos is None
    assert "resumen" in errores


def test_camino_valido_con_opcionales_vacios():
    datos = {"enunciado": "Invertir una lista", "idea_clave": "Tres punteros"}
    campos, errores = validar_campos("camino", datos)
    assert errores == {}
    assert campos["camino"] == ""


def test_camino_sin_idea_clave_se_rechaza():
    datos = {"enunciado": "Invertir una lista", "idea_clave": ""}
    campos, errores = validar_campos("camino", datos)
    assert campos is None
    assert "idea_clave" in errores


def test_tipo_desconocido_se_rechaza():
    campos, errores = validar_campos("poema", {})
    assert campos is None
    assert "tipo" in errores


def test_campo_con_solo_espacios_se_rechaza():
    datos = {"preguntas_clave": "x", "notas": "   ", "resumen": "z"}
    campos, errores = validar_campos("cornell", datos)
    assert campos is None
    assert "notas" in errores


def test_se_quitan_los_espacios_de_los_costados():
    datos = {"preguntas_clave": "x", "notas": "y", "resumen": "  hola  "}
    campos, errores = validar_campos("cornell", datos)
    assert campos["resumen"] == "hola"
