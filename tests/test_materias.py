def test_inicio_responde(client):
    respuesta = client.get("/")
    assert respuesta.status_code == 200


def test_lista_vacia_muestra_mensaje(client):
    respuesta = client.get("/materias")
    assert "Todavía no hay materias" in respuesta.text


def test_crear_materia_aparece_en_la_lista(client):
    client.post("/materias", data={"nombre": "Programación"})
    respuesta = client.get("/materias")
    assert "Programación" in respuesta.text


def test_nombre_vacio_no_crea_materia(client):
    client.post("/materias", data={"nombre": "   "})
    respuesta = client.get("/materias")
    assert "Todavía no hay materias" in respuesta.text


def test_materia_inexistente_da_404(client):
    respuesta = client.get("/materias/999")
    assert respuesta.status_code == 404


def test_tema_pertenece_solo_a_su_materia(client):
    client.post("/materias", data={"nombre": "Programación"})
    client.post("/materias", data={"nombre": "Matemática"})

    client.post("/materias/1/temas", data={"nombre": "Bucles"})

    assert "Bucles" in client.get("/materias/1").text
    assert "Bucles" not in client.get("/materias/2").text
