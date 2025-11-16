from datetime import date, timedelta
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
def _email():
    return f"t{uuid4().hex[:8]}@test.com"


def _isbn():
    return uuid4().hex[:10]


def criar_usuario(client):
    r = client.post("/usuarios", json={"nome": "U", "email": _email()})
    assert r.status_code == 201
    return r.json()


def criar_livro(client):
    r = client.post("/livros", json={"titulo": "L", "isbn": _isbn()})
    assert r.status_code == 201
    return r.json()


# -------------------------------------------------------------------
# TESTES DE EMPRÉSTIMOS — API
# -------------------------------------------------------------------

def test_criar_emprestimo_ok(client):
    """
    Fluxo feliz: empréstimo criado com sucesso.
    """
    u = criar_usuario(client)
    l = criar_livro(client)
    hoje = date.today()

    r = client.post("/emprestimos", json={
        "usuario_id": u["id"],
        "livro_id": l["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7))
    })

    assert r.status_code == 201
    emp = r.json()
    assert emp["usuario_id"] == u["id"]
    assert emp["livro_id"] == l["id"]


def test_emprestimo_livro_indisponivel(client):
    """
    Não pode emprestar um livro já emprestado.
    """
    u1 = criar_usuario(client)
    u2 = criar_usuario(client)
    l = criar_livro(client)
    hoje = date.today()

    # Primeiro empréstimo deixa o livro indisponível
    r1 = client.post("/emprestimos", json={
        "usuario_id": u1["id"],
        "livro_id": l["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7))
    })
    assert r1.status_code == 201

    # Segundo deve falhar
    r2 = client.post("/emprestimos", json={
        "usuario_id": u2["id"],
        "livro_id": l["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7))
    })

    assert r2.status_code in (400, 409, 422)
