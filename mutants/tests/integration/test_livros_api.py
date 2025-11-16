# testes/integration/test_regras_livro_api.py

import pytest
from uuid import uuid4

from aplicacao.db.database import resetar_banco


# -------------------------------------------------------------------
# FIXTURE DE ROLLBACK
# -------------------------------------------------------------------
@pytest.fixture(autouse=True, scope="function")
def limpar_banco_antes_de_cada_teste():
    resetar_banco()


# -------------------------------------------------------------------
# HELPERS
# -------------------------------------------------------------------
def _isbn():
    return uuid4().hex[:10]


# -------------------------------------------------------------------
# TESTES
# -------------------------------------------------------------------

def test_criar_livro_ok(client):
    r = client.post("/livros", json={"titulo": "Dom Quixote", "isbn": _isbn()})
    assert r.status_code == 201
    body = r.json()
    assert body["titulo"] == "Dom Quixote"
    assert "id" in body


def test_criar_livro_invalido(client):
    r = client.post("/livros", json={"titulo": "", "isbn": ""})
    assert r.status_code == 422


def test_listar_livros(client):
    client.post("/livros", json={"titulo": "A", "isbn": _isbn()})
    r = client.get("/livros")
    assert r.status_code == 200
    body = r.json()
    assert isinstance(body, list)
    assert len(body) >= 1


def test_atualizar_livro_ok(client):
    l = client.post("/livros", json={"titulo": "X", "isbn": _isbn()}).json()
    r = client.patch(f"/livros/{l['id']}", json={"titulo": "Novo"})
    assert r.status_code == 200
    assert r.json()["titulo"] == "Novo"


def test_atualizar_livro_404(client):
    r = client.patch("/livros/99999", json={"titulo": "X"})
    assert r.status_code == 404


def test_remover_livro_ok(client):
    l = client.post("/livros", json={"titulo": "Del", "isbn": _isbn()}).json()
    r = client.delete(f"/livros/{l['id']}")
    assert r.status_code == 204


def test_remover_livro_inexistente(client):
    r = client.delete("/livros/99999")
    assert r.status_code == 404
