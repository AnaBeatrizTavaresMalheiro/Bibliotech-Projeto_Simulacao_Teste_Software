import pytest
from fastapi.testclient import TestClient
from datetime import date, timedelta

from aplicacao.server.main import app

client = TestClient(app)

# ================================================================
# HELPERS
# ================================================================

def criar_usuario(email="user@example.com"):
    r = client.post("/usuarios/", json={
        "nome": "Teste",
        "email": email
    })
    assert r.status_code in (200, 201)
    return r.json()


def criar_livro(isbn="0000"):
    r = client.post("/livros/", json={
        "titulo": "Livro Teste",
        "isbn": isbn
    })
    assert r.status_code in (200, 201)
    return r.json()


def criar_emprestimo(uid, lid,
                     data_emprestimo="2025-01-01",
                     data_prevista="2025-01-10"):
    r = client.post("/emprestimos/", json={
        "usuario_id": uid,
        "livro_id": lid,
        "data_emprestimo": data_emprestimo,
        "data_devolucao_prevista": data_prevista,
    })
    assert r.status_code in (200, 201)
    return r.json()


# =======================================================================
# 1) CRIAR USUÁRIO VÁLIDO
# =======================================================================

def test_func_criar_usuario_valido():
    r = client.post("/usuarios/", json={
        "nome": "Ana",
        "email": "ana@x.com"
    })
    assert r.status_code == 201
    assert r.json()["email"] == "ana@x.com"


# =======================================================================
# 2) BLOQUEAR E-MAIL DUPLICADO
# =======================================================================

def test_func_criar_usuario_duplicado():
    client.post("/usuarios/", json={"nome": "A", "email": "dup@x.com"})
    r = client.post("/usuarios/", json={"nome": "B", "email": "dup@x.com"})
    assert r.status_code == 400


# =======================================================================
# 3) CRIAR LIVRO DISPONÍVEL
# =======================================================================

def test_func_criar_livro_valido():
    r = client.post("/livros/", json={"titulo": "Livro A", "isbn": "12345"})
    assert r.status_code == 201
    assert r.json()["isbn"] == "12345"


# =======================================================================
# 4) CRIAR EMPRÉSTIMO VÁLIDO
# =======================================================================

def test_func_emprestimo_valido():
    u = criar_usuario("emprestimo@x.com")
    l = criar_livro("ISBN-EMP-1")

    r = client.post("/emprestimos/", json={
        "usuario_id": u["id"],
        "livro_id": l["id"],
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    assert r.status_code == 201
    assert r.json()["usuario_id"] == u["id"]


# =======================================================================
# 5) BLOQUEAR EMPRÉSTIMO DE LIVRO INDISPONÍVEL
# =======================================================================

def test_func_emprestimo_livro_indisponivel():
    u = criar_usuario("multi@x.com")
    l = criar_livro("ISBN-UNICO")

    # primeiro empréstimo deixa o livro indisponível
    criar_emprestimo(u["id"], l["id"])

    # tenta emprestar de novo
    r = client.post("/emprestimos/", json={
        "usuario_id": u["id"],
        "livro_id": l["id"],
        "data_emprestimo": "2025-01-05",
        "data_devolucao_prevista": "2025-01-12"
    })

    assert r.status_code in (400, 422, 500)


# =======================================================================
# 6) USUÁRIO COM MULTA NÃO PODE EMPRESTAR
# =======================================================================

def test_func_usuario_com_multa():
    # criando usuário COM multa
    r_user = client.post("/usuarios/", json={
        "nome": "Joao",
        "email": "multa@x.com",
        "possui_multa_aberta": True
    })
    assert r_user.status_code in (200, 201)
    uid = r_user.json()["id"]

    l = criar_livro("ISBN-MULTA")

    r = client.post("/emprestimos/", json={
        "usuario_id": uid,
        "livro_id": l["id"],
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-05",
    })

    assert r.status_code in (400, 422, 500)


# =======================================================================
# 7) DEVOLVER LIVRO SEM ATRASO
# =======================================================================

def test_func_devolver_sem_atraso():
    u = criar_usuario("dev1@x.com")
    l = criar_livro("DEV-S1")

    e = criar_emprestimo(u["id"], l["id"])

    r = client.post(f"/emprestimos/{e['id']}/devolucao", json={
        "data_devolucao_real": "2025-01-05"
    })

    assert r.status_code == 200
    assert r.json()["dias_atraso"] == 0


# =======================================================================
# 8) DEVOLVER LIVRO COM ATRASO
# =======================================================================

def test_func_devolver_com_atraso():
    u = criar_usuario("dev2@x.com")
    l = criar_livro("DEV-A1")

    e = criar_emprestimo(u["id"], l["id"],
        data_emprestimo="2025-01-01",
        data_prevista="2025-01-05"
    )

    r = client.post(f"/emprestimos/{e['id']}/devolucao", json={
        "data_devolucao_real": "2025-01-08"
    })

    assert r.status_code == 200
    assert r.json()["dias_atraso"] == 3
    assert r.json()["valor_multa"] == 4.5


# =======================================================================
# 9) BLOQUEAR DEVOLUÇÃO DUPLICADA
# =======================================================================

def test_func_devolver_duplicado():
    u = criar_usuario("devdupl@x.com")
    l = criar_livro("DEV-D1")

    e = criar_emprestimo(u["id"], l["id"])

    # primeira
    client.post(f"/emprestimos/{e['id']}/devolucao", json={
        "data_devolucao_real": "2025-01-04"
    })

    # segunda
    r2 = client.post(f"/emprestimos/{e['id']}/devolucao", json={
        "data_devolucao_real": "2025-01-05"
    })

    assert r2.status_code in (400, 422, 500)


# =======================================================================
# 10) USUÁRIO COM EMPRÉSTIMO ATIVO NÃO PODE SER REMOVIDO
# =======================================================================

def test_func_usuario_nao_remove_com_emprestimo():
    u = criar_usuario("remover@x.com")
    l = criar_livro("R-EMP-A1")

    criar_emprestimo(u["id"], l["id"])

    r = client.delete(f"/usuarios/{u['id']}")
    assert r.status_code in (400, 422, 500)
