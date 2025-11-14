# testes/fixtures/conftest_integration.py

import os
os.environ["TESTING"] = "1"  #

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from src.server.main import app
from src.db import modelos
from src.server.rotas import obter_sessao as rotas_get_sessao

# --------------------------------------------------------
# Engine em memória e sessão para testes
# --------------------------------------------------------
@pytest.fixture(scope="function")
def engine():
    """Cria engine SQLite em memória para testes."""
    engine = create_engine("sqlite:///:memory:", echo=False)
    SQLModel.metadata.create_all(engine)
    return engine

@pytest.fixture(scope="function")
def session(engine):
    """Sessão ligada ao engine de teste."""
    with Session(engine) as s:
        yield s

# --------------------------------------------------------
# TestClient com dependência de sessão sobrescrita
# --------------------------------------------------------
@pytest.fixture(scope="function")
def client(engine):
    """TestClient usando engine em memória, sem tocar no DB real."""
    def get_test_sessao():
        with Session(engine) as s:
            yield s

    # Sobrescreve a dependência do endpoint
    app.dependency_overrides[rotas_get_sessao] = get_test_sessao

    # Remove startup que tocaria no banco real
    app.router.on_startup.clear()

    with TestClient(app) as c:
        yield c

    # Limpa sobrescritas
    app.dependency_overrides.clear()

# --------------------------------------------------------
# Acesso direto à sessão do client (para helpers)
# --------------------------------------------------------
@pytest.fixture
def sessao(client):
    """Permite acesso direto à sessão usada pelo client."""
    dep = app.dependency_overrides[rotas_get_sessao]
    return next(dep())

# --------------------------------------------------------
# Helpers para criar dados no banco de teste
# --------------------------------------------------------
@pytest.fixture
def criar_usuario(sessao):
    """Helper para criar usuários no banco de teste."""
    def _criar(nome, email, possui_multa=False):
        usuario = modelos.Usuario(
            nome=nome,
            email=email,
            possui_multa_aberta=possui_multa,
            qtd_emprestimo=0
        )
        sessao.add(usuario)
        sessao.commit()
        sessao.refresh(usuario)
        return usuario
    return _criar

@pytest.fixture
def criar_livro(sessao):
    """Helper para criar livros no banco de teste."""
    def _criar(titulo, disponivel=True):
        livro = modelos.Livro(
            titulo=titulo,
            isbn=f"TEST-{titulo[:5]}",  # ISBN fake para testes
            disponivel=disponivel
        )
        sessao.add(livro)
        sessao.commit()
        sessao.refresh(livro)
        return livro
    return _criar
