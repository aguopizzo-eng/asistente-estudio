import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from app.database import get_session
from app.main import app


@pytest.fixture(name="client")
def client_fixture():
    # Base de datos en memoria: se crea vacía para cada test y desaparece al terminar.
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)

    def get_session_de_prueba():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = get_session_de_prueba
    yield TestClient(app)
    app.dependency_overrides.clear()
