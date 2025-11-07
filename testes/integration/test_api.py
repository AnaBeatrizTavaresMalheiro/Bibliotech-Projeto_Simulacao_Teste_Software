# testes/integration/test_api.py

import pytest
from fastapi.testclient import TestClient

# ----------------------------
# Helper para criar usuário via API
# ----------------------------
def criar_usuario(client, nome="Teste", email="teste@test.com"):
    """Cria um usuário via API e retorna o response."""
    return client.post("/usuarios", json={"nome": nome, "email": email})

def criar_livro(client, titulo="Livro Teste", isbn="12345"):
    """Cria um livro via API e retorna o response."""
    return client.post("/livros", json={"titulo": titulo, "isbn": isbn})

# ----------------------------
# Testes CRUD de usuários
# ----------------------------
def test_criar_usuario(client: TestClient):
    response = criar_usuario(client, "Ana", "ana@test.com")
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Ana"
    assert data["email"] == "ana@test.com"
    assert "id" in data

def test_criar_usuario_invalido(client: TestClient):
    response = criar_usuario(client, "", "invalid-email")
    assert response.status_code == 422

def test_criar_usuario_email_duplicado(client: TestClient):
    criar_usuario(client, "A", "a@a.com")
    res = criar_usuario(client, "B", "a@a.com")
    assert res.status_code == 400

def test_get_usuario(client: TestClient):
    criar_usuario(client, "Alice", "alice@test.com")
    response = client.get("/usuarios", params={"nome": "Alice"})
    assert response.status_code == 200
    data = response.json()
    assert any(u["nome"] == "Alice" for u in data)

def test_get_usuario_inexistente(client: TestClient):
    response = client.get("/usuarios/999")
    assert response.status_code == 404

def test_atualizar_usuario(client: TestClient):
    res = criar_usuario(client, "Daniel", "daniel@test.com")
    user_id = res.json()["id"]
    response = client.patch(
        f"/usuarios/{user_id}",
        json={"nome": "Daniel Silva", "email": "daniel.silva@test.com"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Daniel Silva"
    assert data["email"] == "daniel.silva@test.com"

def test_atualizar_usuario_inexistente(client: TestClient):
    response = client.patch(
        "/usuarios/9999",
        json={"nome": "Não existe", "email": "nao@test.com"}
    )
    assert response.status_code == 404

def test_deletar_usuario(client: TestClient):
    res = criar_usuario(client, "Carlos", "carlos@test.com")
    user_id = res.json()["id"]

    response = client.delete(f"/usuarios/{user_id}")
    assert response.status_code == 204

    # Confirma que usuário foi deletado
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 404

def test_deletar_usuario_inexistente(client: TestClient):
    response = client.delete("/usuarios/9999")
    assert response.status_code == 404

def test_listar_usuarios_com_filtro(client: TestClient):
    criar_usuario(client, "Daniel", "daniel@test.com")
    criar_usuario(client, "Daniella", "daniella@test.com")

    response = client.get("/usuarios", params={"nome": "Daniel"})
    assert response.status_code == 200
    data = response.json()
    assert all("Daniel" in u["nome"] for u in data)

# ----------------------------
# Testes CRUD de livros
# ----------------------------
def test_criar_livro_valido(client: TestClient):
    res = criar_livro(client, "Dom Quixote", "11111")
    assert res.status_code == 201
    data = res.json()
    assert data["titulo"] == "Dom Quixote"
    assert data["isbn"] == "11111"
    assert data["disponivel"] is True

def test_criar_livro_invalido(client: TestClient):
    res = criar_livro(client, "", "12")
    assert res.status_code == 422

def test_listar_livros(client: TestClient):
    criar_livro(client, "Livro A", "12345")
    res = client.get("/livros")
    assert res.status_code == 200
    data = res.json()
    assert any(l["titulo"] == "Livro A" for l in data)

def test_atualizar_livro(client: TestClient):
    res = criar_livro(client, "Livro Update", "54321")
    livro_id = res.json()["id"]
    response = client.patch(f"/livros/{livro_id}", json={"titulo": "Novo Título"})
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Novo Título"

def test_atualizar_livro_inexistente(client: TestClient):
    res = client.patch("/livros/9999", json={"titulo": "Não existe"})
    assert res.status_code == 404

def test_deletar_livro(client: TestClient):
    res = criar_livro(client, "Livro Del", "55555")
    livro_id = res.json()["id"]
    res_del = client.delete(f"/livros/{livro_id}")
    assert res_del.status_code == 204

def test_deletar_livro_inexistente(client: TestClient):
    res = client.delete("/livros/9999")
    assert res.status_code in (404, 400)
