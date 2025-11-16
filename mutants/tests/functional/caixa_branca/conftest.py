import pytest
from sqlmodel import Session
from aplicacao.db.sessao import engine
from aplicacao.db.database import resetar_banco
from fastapi.testclient import TestClient
from aplicacao.server.main import app

@pytest.fixture(autouse=True)
def rollback():
    resetar_banco()


@pytest.fixture
def sessao_real():
    s = Session(engine)
    yield s
    s.close()

@pytest.fixture(scope="function")
def client():
    resetar_banco()
    return TestClient(app)


@pytest.fixture(scope="function")
def reset_db():
    resetar_banco()