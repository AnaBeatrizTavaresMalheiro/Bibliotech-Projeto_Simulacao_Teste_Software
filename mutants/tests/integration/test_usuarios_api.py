# testes/integration/test_regras_usuario_api.py

import pytest
from uuid import uuid4

from aplicacao.db.database import resetar_banco


# -------------------------------------------------------------------
# FIXTURES
# -------------------------------------------------------------------

@pytest.fixture(autouse=True, scope="function")
def limpar_banco_antes_de_cada_teste():
    resetar_banco()
    yield


@pytest.fixture
def _email():
    """Gera e-mail único por teste."""
    return lambda: f"u{uuid4().hex[:8]}@teste.com"


# -------------------------------------------------------------------
# TESTES DE USUÁRIO
# -------------------------------------------------------------------

def test_criar_usuario_ok(client, _email):
    r = client.post("/usuarios", json={"nome": "Ana", "email": _email()})
    assert r.status_code == 201
    body = r.json()
    assert body["id"] > 0
    assert body["nome"] == "Ana"


def test_criar_usuario_email_duplicado(client, _email):
    email = _email()

    client.post("/usuarios", json={"nome": "A", "email": email})
    r = client.post("/usuarios", json={"nome": "B", "email": email})

    assert r.status_code == 400


def test_listar_usuarios(client, _email):
    client.post("/usuarios", json={"nome": "X", "email": _email()})
    r = client.get("/usuarios")

    assert r.status_code == 200
    lista = r.json()
    assert isinstance(lista, list)
    assert len(lista) >= 1


def test_atualizar_usuario_ok(client, _email):
    u = client.post("/usuarios", json={"nome": "A", "email": _email()}).json()

    novo_email = _email()
    r = client.patch(
        f"/usuarios/{u['id']}",
        json={"nome": "Ana Maria", "email": novo_email}
    )

    assert r.status_code == 200
    assert r.json()["nome"] == "Ana Maria"
    assert r.json()["email"] == novo_email


def test_atualizar_usuario_404(client):
    r = client.patch("/usuarios/99999", json={"nome": "X"})

    assert r.status_code == 404


def test_deletar_usuario_ok(client, _email):
    u = client.post("/usuarios", json={"nome": "Z", "email": _email()}).json()

    r = client.delete(f"/usuarios/{u['id']}")
    assert r.status_code == 204

    r2 = client.get(f"/usuarios/{u['id']}")
    assert r2.status_code == 404


def test_deletar_usuario_inexistente(client):
    r = client.delete("/usuarios/99999")

    assert r.status_code == 404
