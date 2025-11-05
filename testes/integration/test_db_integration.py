import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from db import conexao, modelos


def test_criar_tabelas_sqlite(tmp_path):
    db_path = tmp_path / "test.db"
    engine = conexao.criar_engine(f"sqlite:///{db_path}")
    assert engine is not None

def test_inserir_usuario_simplificado():
    usuario = modelos.Usuario(nome="Maria", email="maria@test.com")
    assert usuario.nome == "Maria"

def test_criar_usuario(client):
    response = client.post("/usuarios", json={
        "nome": "Ana",
        "email": "ana@test.com"
    })
    assert response.status_code == 201
    json_resp = response.json()
    assert json_resp["nome"] == "Ana"
    assert json_resp["email"] == "ana@test.com"
    

def test_criar_usuario_invalido(client):
    response = client.post("/usuarios", json={
        "nome": "",  # nome vazio
        "email": "invalid-email"
    })
    assert response.status_code == 422

def test_get_usuario(client):
    # Cria usuário
    client.post("/usuarios", json={"nome": "Alice", "email": "alice@test.com"})

    # Faz a requisição
    response = client.get("/usuarios", params={"nome": "Alice"})
    assert response.status_code == 200
    data = response.json()
    assert any(u["nome"] == "Alice" for u in data)

def test_get_usuario_inexistente(client):
    response = client.get("/usuarios/999")
    assert response.status_code == 404

def test_deletar_usuario(client):
    # Cria usuário
    response = client.post("/usuarios", json={"nome": "Carlos", "email": "carlos@test.com"})
    user_id = response.json()["id"]

    # Deleta usuário
    response = client.delete(f"/usuarios/{user_id}")
    assert response.status_code == 204

    # Verifica se realmente foi deletado
    response = client.get(f"/usuarios/{user_id}")
    assert response.status_code == 404

def test_deletar_usuario_inexistente(client):
    response = client.delete("/usuarios/9999")
    assert response.status_code == 404

def test_listar_usuarios_com_filtro(client):
    # Cria usuários
    client.post("/usuarios", json={"nome": "Daniel", "email": "daniel@test.com"})
    client.post("/usuarios", json={"nome": "Daniella", "email": "daniella@test.com"})

    # Filtra por nome
    response = client.get("/usuarios", params={"nome": "Daniel"})
    assert response.status_code == 200
    data = response.json()
    assert all("Daniel" in u["nome"] for u in data)

def test_criar_usuario_email_invalido(client):
    response = client.post("/usuarios", json={"nome": "Lucas", "email": "lucas#test.com"})
    assert response.status_code == 422

