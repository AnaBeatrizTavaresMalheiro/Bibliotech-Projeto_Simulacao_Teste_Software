# testes/integration/conftest.py

import pytest
from fastapi.testclient import TestClient

from aplicacao.server.main import app
from aplicacao.db.database import resetar_banco


@pytest.fixture(autouse=True, scope="function")
def limpar_banco_antes_de_cada_teste():
    resetar_banco()
    yield  # nada depois, mas poderíamos logar se quiséssemos
    # opcional: resetar aqui também, mas geralmente não precisa


@pytest.fixture
def client():
    """
    Cliente FastAPI para testes de integração.
    """
    return TestClient(app)
