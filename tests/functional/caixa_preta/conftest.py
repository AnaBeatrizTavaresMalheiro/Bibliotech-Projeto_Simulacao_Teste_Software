import pytest
from fastapi.testclient import TestClient
from aplicacao.server.main import app
from aplicacao.db.database import resetar_banco


# --------------------------------------
# FIXTURE 
# --------------------------------------
@pytest.fixture
def client():
    return TestClient(app)


# --------------------------------------
# FIXTURE 
# --------------------------------------
@pytest.fixture(autouse=True, scope="function")
def limpar_banco():
    resetar_banco()
