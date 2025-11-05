import sys, os
import pytest
from fastapi.testclient import TestClient
import random
from sqlmodel import SQLModel
from db.conexao import motor

# Ajusta o path para importar db, server, etc
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from server.main import app
from db import modelos, conexao
from server import regras  # funções de regras.py

@pytest.fixture(autouse=True)
def limpa_banco():
    SQLModel.metadata.drop_all(motor)
    SQLModel.metadata.create_all(motor)
    yield

client = TestClient(app)

# ----------------------------
# Testes main.py (inicialização)
# ----------------------------
def test_app_importavel():
    assert app is not None
    # Supondo que haja rota de healthcheck ou qualquer rota simples
    response = client.get("/usuarios")  # ou outra rota existente
    assert response.status_code in (200, 404)

# ----------------------------
# Testes regras.py
# ----------------------------
def test_validar_email():
    # Exemplo genérico de função de validação
    if hasattr(regras, "validar_email"):
        assert regras.validar_email("teste@test.com") is True
        assert regras.validar_email("teste.com") is False

def test_outra_regra():
    # Supondo função exemplo calcular_idade
    if hasattr(regras, "calcular_idade"):
        from datetime import date
        assert regras.calcular_idade(date(2000, 1, 1)) == date.today().year - 2000

# ----------------------------
# Função helper para criar usuário
# ----------------------------
def criar_usuario(nome="Teste", email="teste@test.com"):
    return client.post("/usuarios", json={"nome": nome, "email": email})

# ----------------------------
# Testes rotas CRUD
# ----------------------------
def test_criar_usuario_valido():
    response = criar_usuario("Alice", "alice@test.com")
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Alice"
    assert data["email"] == "alice@test.com"

def test_criar_usuario_invalido():
    response = criar_usuario("", "email-invalido")
    assert response.status_code == 422

def test_listar_usuarios():
    # Cria usuário via rota POST
    criar_usuario("Bob", "bob@test.com")

    # Lista todos usuários
    response = client.get("/usuarios", params={"nome": "Bob"})
    assert response.status_code == 200
    data = response.json()
    
    # Verifica se Bob está na lista
    assert any(u["nome"] == "Bob" for u in data), f"Usuários retornados: {data}"


def test_get_usuario_existente():
    res = criar_usuario("Carol", "carol@test.com")
    user_id = res.json()["id"]
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 200
    assert response.json()["nome"] == "Carol"

def test_get_usuario_inexistente():
    response = client.get("/usuarios/9999")
    assert response.status_code == 404

def test_atualizar_usuario():
    res = criar_usuario("Daniel", "daniel@test.com")
    user_id = res.json()["id"]

    response = client.patch(
        f"/usuarios/{user_id}",
        json={"nome": "Daniel Silva", "email": "daniel.silva@test.com"}
    )

    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Daniel Silva"
    assert data["email"] == "daniel.silva@test.com"


def test_atualizar_usuario_inexistente():
    response = client.patch(
        "/usuarios/9999",  # usuário inexistente
        json={"nome": "Não existe", "email": "nao@test.com"}
    )
    assert response.status_code == 404

def test_deletar_usuario():
    res = criar_usuario("Eduardo", "eduardo@test.com")
    user_id = res.json()["id"]
    response = client.delete(f"/usuarios/{user_id}")
    assert response.status_code == 204
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 404

def test_deletar_usuario_inexistente():
    response = client.delete("/usuarios/9999")
    assert response.status_code == 404

def test_listar_usuarios_com_filtro():
    criar_usuario("Fernanda", "fernanda@test.com")
    criar_usuario("Fernando", "fernando@test.com")
    response = client.get("/usuarios", params={"nome": "Fernanda"})
    assert response.status_code == 200
    data = response.json()
    assert all("Fernanda" in u["nome"] for u in data)

# ----------------------------
# Testes SQLModel direto
# ----------------------------

from sqlmodel import Session, SQLModel
from db import modelos
from db.conexao import criar_engine

def test_inserir_e_consultar_usuario_sqlmodel():
    # Cria engine em memória
    engine = criar_engine("sqlite:///:memory:")

    # Cria todas as tabelas a partir dos modelos
    SQLModel.metadata.create_all(engine)

    # Cria sessão
    with Session(engine) as session:
        # Cria usuário
        user = modelos.Usuario(nome="TesteDB", email="testedb@test.com")
        session.add(user)
        session.commit()
        session.refresh(user)

        # Recupera e testa
        retrieved = session.get(modelos.Usuario, user.id)
        assert retrieved is not None
        assert retrieved.nome == "TesteDB"
        assert retrieved.email == "testedb@test.com"

# Helper para criar livro
def criar_livro(titulo="Livro Teste", isbn=None):
    if isbn is None:
        isbn = f"{random.randint(10000, 99999)}"
    return client.post("/livros", json={"titulo": titulo, "isbn": isbn})

def test_criar_livro_valido():
    res = criar_livro("Dom Quixote", "11111")
    assert res.status_code == 201
    data = res.json()
    assert data["titulo"] == "Dom Quixote"
    assert data["isbn"] == "11111"
    assert data["disponivel"] is True

def test_criar_livro_invalido():
    res = criar_livro("", "12")
    assert res.status_code == 422

def test_listar_livros():
    res = criar_livro("Livro A")
    assert res.status_code == 201

    res2 = client.get("/livros")
    assert res2.status_code == 200
    data = res2.json()
    assert any(l["titulo"] == "Livro A" for l in data)

def test_atualizar_livro():
    isbn_unico = f"ISBN-{random.randint(1000,9999)}"
    res = criar_livro("Livro Update", isbn_unico)
    livro_id = res.json()["id"]

    response = client.patch(f"/livros/{livro_id}", json={"titulo": "Novo Título"})
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Novo Título"

def test_atualizar_livro_inexistente():
    res_patch = client.patch("/livros/9999", json={"titulo": "Não existe"})
    assert res_patch.status_code == 404

def test_deletar_livro():
    res = criar_livro("Livro Del", "55555")
    livro_id = res.json()["id"]

    res_del = client.delete(f"/livros/{livro_id}")
    assert res_del.status_code == 204

    # Verifica se o livro não aparece mais na lista
    res_list = client.get("/livros")
    assert res_list.status_code == 200
    livros = res_list.json()
    assert all(l["id"] != livro_id for l in livros)

