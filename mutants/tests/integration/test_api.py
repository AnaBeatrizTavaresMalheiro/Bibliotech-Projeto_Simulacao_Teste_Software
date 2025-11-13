# testes/integration/test_api.py

from datetime import date, timedelta
import uuid
from fastapi.testclient import TestClient
import pytest

from src.db.criar_schemas import limpar_banco_via_api

# =============================================================================
# Helpers
# =============================================================================
def _email() -> str:
    return f"t{uuid.uuid4().hex[:10]}@test.com"

def _isbn() -> str:
    return uuid.uuid4().hex[:10]

def criar_usuario(client: TestClient, nome="Teste", email=None, multa: bool = False):
    if email is None:
        email = _email()
    return client.post("/usuarios", json={
        "nome": nome,
        "email": email,
        "possuimulta_aberta": multa  # aceita chave desconhecida; back-end ignora? Se necessário, troque pela correta.
    })  # se seu schema exige exatamente 'possui_multa_aberta', mude a chave acima.

def criar_livro(client: TestClient, titulo="Livro Teste", isbn=None, disponivel=True):
    if isbn is None:
        isbn = _isbn()
    return client.post("/livros", json={
        "titulo": titulo,
        "isbn": isbn,
        "disponivel": disponivel
    })

# =============================================================================
# Usuários (padrão único: limpar -> arrange -> act -> assert)
# =============================================================================
def test_criar_usuario(client: TestClient):
    limpar_banco_via_api()
    r = client.post("/usuarios", json={"nome": "Ana", "email": "ana@test.com"})
    assert r.status_code == 201
    body = r.json()
    assert body["nome"] == "Ana"
    assert body["email"] == "ana@test.com"
    assert "id" in body

def test_criar_usuario_invalido(client: TestClient):
    limpar_banco_via_api()
    r = client.post("/usuarios", json={"nome": "", "email": "invalid-email"})
    assert r.status_code == 422

def test_criar_usuario_email_duplicado(client: TestClient):
    limpar_banco_via_api()
    client.post("/usuarios", json={"nome": "A", "email": "a@a.com"})
    r = client.post("/usuarios", json={"nome": "B", "email": "a@a.com"})
    assert r.status_code == 400

def test_get_usuario_por_filtro(client: TestClient):
    limpar_banco_via_api()
    client.post("/usuarios", json={"nome": "Alice", "email": "alice@test.com"})
    r = client.get("/usuarios", params={"nome": "Alice"})
    assert r.status_code == 200
    assert any(u["nome"] == "Alice" for u in r.json())

def test_get_usuario_inexistente(client: TestClient):
    limpar_banco_via_api()
    r = client.get("/usuarios/999999")
    assert r.status_code == 404

def test_atualizar_usuario(client: TestClient):
    limpar_banco_via_api()
    res = client.post("/usuarios", json={"nome": "Daniel", "email": "daniel@test.com"})
    uid = res.json()["id"]
    r = client.patch(f"/usuarios/{uid}", json={"nome": "Daniel Silva", "email": "daniel.silva@test.com"})
    assert r.status_code == 200
    body = r.json()
    assert body["nome"] == "Daniel Silva"
    assert body["email"] == "daniel.silva@test.com"

def test_atualizar_usuario_404(client: TestClient):
    limpar_banco_via_api()
    r = client.patch("/usuarios/999999", json={"nome": "X"})
    assert r.status_code in (404, 400)

def test_deletar_usuario(client: TestClient):
    limpar_banco_via_api()
    res = client.post("/usuarios", json={"nome": "Carlos", "email": "carlos@test.com"})
    uid = res.json()["id"]
    r_del = client.delete(f"/usuarios/{uid}")
    assert r_del.status_code == 204
    r_get = client.get(f"/usuarios/{uid}")
    assert r_get.status_code == 404

def test_deletar_usuario_inexistente(client: TestClient):
    limpar_banco_via_api()
    r = client.delete("/usuarios/999999")
    assert r.status_code == 404

def test_listar_usuarios_com_filtro_e_ordenacao(client: TestClient):
    limpar_banco_via_api()
    client.post("/usuarios", json={"nome": "Daniel", "email": _email()})
    client.post("/usuarios", json={"nome": "Daniella", "email": _email(), "possuimulta_aberta": True})
    client.post("/usuarios", json={"nome": "Outro", "email": _email()})

    r = client.get("/usuarios", params={"nome": "Dani", "ordenar_por": "nome", "ordem": "desc"})
    assert r.status_code == 200
    nomes = [u["nome"] for u in r.json()]
    assert all("Dani" in n for n in nomes)
    assert nomes == sorted(nomes, reverse=True)

    r2 = client.get("/usuarios", params={"possui_multa_aberta": "true"})
    assert r2.status_code == 200
    assert all(u["possui_multa_aberta"] is True for u in r2.json())

# =============================================================================
# Livros
# =============================================================================
def test_criar_livro_valido(client: TestClient):
    limpar_banco_via_api()
    r = client.post("/livros", json={"titulo": "Dom Quixote", "isbn": "11111"})
    assert r.status_code == 201
    body = r.json()
    assert body["titulo"] == "Dom Quixote"
    assert body["isbn"] == "11111"
    assert body["disponivel"] is True

def test_criar_livro_invalido(client: TestClient):
    limpar_banco_via_api()
    r = client.post("/livros", json={"titulo": "", "isbn": "12"})
    assert r.status_code == 422

def test_listar_livros(client: TestClient):
    limpar_banco_via_api()
    client.post("/livros", json={"titulo": "Livro A", "isbn": "12345"})
    r = client.get("/livros")
    assert r.status_code == 200
    assert any(l["titulo"] == "Livro A" for l in r.json())

def test_atualizar_livro(client: TestClient):
    limpar_banco_via_api()
    res = client.post("/livros", json={"titulo": "Livro Update", "isbn": "54321"})
    lid = res.json()["id"]
    r = client.patch(f"/livros/{lid}", json={"titulo": "Novo Título"})
    assert r.status_code == 200
    assert r.json()["titulo"] == "Novo Título"

def test_atualizar_livro_inexistente(client: TestClient):
    limpar_banco_via_api()
    r = client.patch("/livros/999999", json={"titulo": "X"})
    assert r.status_code in (404, 400)

def test_deletar_livro(client: TestClient):
    limpar_banco_via_api()
    res = client.post("/livros", json={"titulo": "Livro Del", "isbn": "55555"})
    lid = res.json()["id"]
    r_del = client.delete(f"/livros/{lid}")
    assert r_del.status_code == 204

def test_deletar_livro_inexistente(client: TestClient):
    limpar_banco_via_api()
    r = client.delete("/livros/999999")
    assert r.status_code in (404, 400)

def test_remover_livro_com_emprestimo_ativo(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    emp = {
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    }
    r_emp = client.post("/emprestimos", json=emp)
    assert r_emp.status_code == 200
    r_del = client.delete(f"/livros/{l['id']}")
    assert r_del.status_code in (400, 409, 422)

def test_listar_livros_vazio(client: TestClient):
    limpar_banco_via_api()
    r = client.get("/livros")
    assert r.status_code == 200
    assert r.json() == []

def test_listar_livros_ordenacao_paginacao(client: TestClient):
    limpar_banco_via_api()
    client.post("/livros", json={"titulo": "A", "isbn": "11111"})
    client.post("/livros", json={"titulo": "B", "isbn": "22222"})
    client.post("/livros", json={"titulo": "C", "isbn": "33333"})
    r = client.get("/livros")
    assert r.status_code == 200
    assert len(r.json()) >= 3
    r2 = client.get("/livros", params={"limit": 2, "offset": 1})
    assert r2.status_code == 200
    assert len(r2.json()) == 2

# =============================================================================
# Empréstimos
# =============================================================================
def test_criar_emprestimo_sucesso(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    r = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    })
    assert r.status_code == 200
    emp = r.json()
    assert emp["livro_id"] == l["id"]
    assert emp["usuario_id"] == u["id"]

def test_criar_emprestimo_livro_indisponivel(client: TestClient):
    limpar_banco_via_api()
    u1 = client.post("/usuarios", json={"nome": "U1", "email": _email()}).json()
    u2 = client.post("/usuarios", json={"nome": "U2", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u1["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    })
    r2 = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u2["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    })
    assert r2.status_code in (400, 409, 422)

def test_criar_emprestimo_usuario_com_multa(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email(), "possui_multa_aberta": True}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    r = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    })
    assert r.status_code in (400, 409,422)

def test_atualizar_emprestimo_prorrogar_sucesso(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    emp = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    }).json()
    nova_prevista = hoje + timedelta(days=10)
    r = client.patch(f"/emprestimos/{emp['id']}", json={"data_devolucao_prevista": str(nova_prevista)})
    assert r.status_code == 200
    assert r.json()["data_devolucao_prevista"] == str(nova_prevista)

def test_atualizar_emprestimo_prorrogar_depois_devolvido_bloqueado(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    emp = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    }).json()
    r_dev = client.post(f"/emprestimos/{emp['id']}/devolucao", json={"data_devolucao_real": str(hoje + timedelta(days=2))})
    assert r_dev.status_code == 200
    r_pr = client.patch(f"/emprestimos/{emp['id']}", json={"data_devolucao_prevista": str(hoje + timedelta(days=10))})
    assert r_pr.status_code in (400, 409,422)

def test_atualizar_emprestimo_404(client: TestClient):
    limpar_banco_via_api()
    r = client.patch("/emprestimos/999999", json={"data_devolucao_prevista": str(date.today())})
    assert r.status_code in (404, 400)

def test_deletar_emprestimo_somente_depois_devolvido(client: TestClient):
    limpar_banco_via_api()
    u = client.post("/usuarios", json={"nome": "U", "email": _email()}).json()
    l = client.post("/livros", json={"titulo": "L", "isbn": _isbn()}).json()
    hoje = date.today()
    emp = client.post("/emprestimos", json={
        "livro_id": l["id"],
        "usuario_id": u["id"],
        "data_emprestimo": str(hoje),
        "data_devolucao_prevista": str(hoje + timedelta(days=7)),
    }).json()
    r_del_ativo = client.delete(f"/emprestimos/{emp['id']}")
    assert r_del_ativo.status_code in (400, 409, 422)
    r_dev = client.post(f"/emprestimos/{emp['id']}/devolucao", json={"data_devolucao_real": str(hoje + timedelta(days=3))})
    assert r_dev.status_code == 200
    r_del_ok = client.delete(f"/emprestimos/{emp['id']}")
    assert r_del_ok.status_code == 204

def test_deletar_emprestimo_inexistente(client: TestClient):
    limpar_banco_via_api()
    r = client.delete("/emprestimos/999999")
    assert r.status_code in (404, 400)

