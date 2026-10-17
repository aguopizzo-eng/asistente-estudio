# Asistente de Estudio

Aplicación web para estudiar con apuntes estructurados (método Cornell, camino mental), una sección de dudas y quizzes generados con IA que se enfocan en tus puntos débiles.

**Estado:** en desarrollo. La Fase 1 (materias y temas) está terminada; sigue la Fase 2 (apuntes).

## Tecnologías

- Python 3.12 o superior
- FastAPI (servidor)
- SQLModel y SQLite (base de datos)
- Jinja2 y Pico.css (pantallas)
- pytest (tests)

## Instalación

Requisitos: Python 3 y Git.

```bash
git clone https://github.com/aguopizzo-eng/asistente-estudio.git
cd asistente-estudio
python3 -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo correrlo

```bash
uvicorn app.main:app --reload
```

Abre http://localhost:8000. La documentación automática de la API está en http://localhost:8000/docs.

La base de datos (`estudio.db`) se crea sola la primera vez que arranca la app.

## Cómo correr los tests

```bash
pytest
```

## Estructura del proyecto

```text
app/
├── main.py          # crea la app y registra las rutas
├── database.py      # conexión a SQLite
├── models.py        # tablas: Materia y Tema
├── templating.py    # configuración de Jinja2
├── routers/         # rutas: materias.py, temas.py
└── templates/       # pantallas HTML
tests/               # tests con pytest
```

## Cómo trabajamos

- Nadie sube código directo a `main`: cada tarea va en su propia rama y se une con un Pull Request.
- Ramas con nombre claro: `feature/...`, `fix/...`, `docs/...`.
- El diseño completo y el plan de trabajo están en el documento de diseño del proyecto.
