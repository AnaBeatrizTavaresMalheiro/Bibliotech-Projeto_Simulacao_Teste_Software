import pytest
from starlette.status import HTTP_303_SEE_OTHER


# -------------------------------
# HOME
# -------------------------------

def test_home_page(client):
    r = client.get("/web/")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


# -------------------------------
# USUÁRIOS
# -------------------------------

def test_listar_usuarios_web(client):
    r = client.get("/web/usuarios")
    assert r.status_code == 200
    assert "text/html" in r.headers["content-type"]


def test_web_usuario_novo_form(client):
    r = client.get("/web/usuarios/novo")
    assert r.status_code == 200


def test_web_criar_usuario_ok(client):
    r = client.post("/web/usuarios/novo", data={
        "nome": "A",
        "email": "a@a.com"
    })
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_criar_usuario_sem_nome(client):
    r = client.post("/web/usuarios/novo", data={
        "nome": "",
        "email": "a@a.com"
    })
    assert r.status_code == 200
    assert "Nome e e-mail são obrigatórios" in r.text


def test_web_criar_usuario_sem_email(client):
    r = client.post("/web/usuarios/novo", data={
        "nome": "A",
        "email": ""
    })
    assert r.status_code == 200
    assert "Nome e e-mail são obrigatórios" in r.text


def test_web_criar_usuario_erro_duplicado(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    r = client.post("/web/usuarios/novo", data={"nome": "B", "email": "a@a.com"})
    assert r.status_code == 200
    assert "Já existe um usuário" in r.text


def test_web_editar_usuario_nao_existe(client):
    r = client.get("/web/usuarios/999/editar", follow_redirects=False)
    assert r.status_code in (200, 404)
    assert "Usuário" in r.text or "404" in r.text


def test_web_editar_usuario_ok(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    r = client.post("/web/usuarios/1/editar", data={"nome": "X", "email": "x@x.com"})
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_update_usuario_duplicado(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/usuarios/novo", data={"nome": "B", "email": "b@b.com"})
    r = client.post("/web/usuarios/2/editar", data={"nome": "B2", "email": "a@a.com"})
    assert r.status_code == 200
    assert "E-mail já está sendo usado" in r.text


def test_web_deletar_usuario_inexistente(client):
    r = client.post("/web/usuarios/999/deletar", follow_redirects=False)
    assert r.status_code in (200, 404)
    assert "Usuário" in r.text


def test_web_deletar_usuario_com_emprestimo_ativo(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    client.post("/emprestimos/", json={
        "usuario_id": 1,
        "livro_id": 1,
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    r = client.post("/web/usuarios/1/deletar")
    assert r.status_code == 200
    assert "Usuário possui empréstimo ativo" in r.text


# -------------------------------
# LIVROS
# -------------------------------

def test_listar_livros_web(client):
    r = client.get("/web/livros")
    assert r.status_code == 200


def test_web_livro_novo_form(client):
    r = client.get("/web/livros/novo")
    assert r.status_code == 200


def test_web_criar_livro_ok(client):
    r = client.post("/web/livros/novo", data={
        "titulo": "Livro Teste",
        "isbn": "12345"
    })
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_criar_livro_sem_titulo(client):
    r = client.post("/web/livros/novo", data={"titulo": "", "isbn": "123"})
    assert r.status_code == 200
    assert "Título e ISBN são obrigatórios" in r.text


def test_web_criar_livro_sem_isbn(client):
    r = client.post("/web/livros/novo", data={"titulo": "A", "isbn": ""})
    assert r.status_code == 200
    assert "Título e ISBN são obrigatórios" in r.text


def test_web_criar_livro_erro_duplicado(client):
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})
    r = client.post("/web/livros/novo", data={"titulo": "L2", "isbn": "111"})
    assert r.status_code == 200
    assert "ISBN" in r.text


def test_web_livro_editar_inexistente(client):
    r = client.get("/web/livros/999/editar", follow_redirects=False)
    assert r.status_code in (200, 404)
    assert "Livro" in r.text


def test_web_livro_editar_ok(client):
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})
    r = client.post("/web/livros/1/editar", data={"titulo": "LL", "isbn": "222"})
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_livro_deletar_com_emprestimo(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    client.post("/emprestimos/", json={
        "usuario_id": 1,
        "livro_id": 1,
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    r = client.post("/web/livros/1/deletar")
    assert r.status_code == 200
    assert "Livro possui empréstimo ativo" in r.text


# -------------------------------
# EMPRÉSTIMOS
# -------------------------------

def test_listar_emprestimos_web(client):
    r = client.get("/web/emprestimos")
    assert r.status_code == 200


def test_web_emprestimo_form(client):
    r = client.get("/web/emprestimos/novo")
    assert r.status_code == 200


def test_web_emprestimo_criar_ok(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    r = client.post("/web/emprestimos/novo", data={
        "usuario_id": 1,
        "livro_id": 1
    })
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_emprestimo_usuario_inexistente(client):
    r = client.post("/web/emprestimos/novo", data={
        "usuario_id": 999,
        "livro_id": 1
    })
    assert r.status_code == 200
    assert "Usuário ou livro não encontrado" in r.text


def test_web_emprestimo_livro_inexistente(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})

    r = client.post("/web/emprestimos/novo", data={
        "usuario_id": 1,
        "livro_id": 999
    })
    assert r.status_code == 200
    assert "Usuário ou livro não encontrado" in r.text


def test_web_emprestimo_livro_indisponivel(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    # cria empréstimo via API
    client.post("/emprestimos/", json={
        "usuario_id": 1,
        "livro_id": 1,
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    r = client.post("/web/emprestimos/novo", data={"usuario_id": 1, "livro_id": 1})
    assert r.status_code == 200
    assert "Livro indisponível" in r.text


def test_web_emprestimo_devolver_ok(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    client.post("/emprestimos/", json={
        "usuario_id": 1,
        "livro_id": 1,
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    r = client.post("/web/emprestimos/1/devolver")
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_emprestimo_devolver_inexistente(client):
    r = client.post("/web/emprestimos/999/devolver")
    assert r.status_code in (200, HTTP_303_SEE_OTHER)


def test_web_emprestimo_devolver_duplicado(client):
    client.post("/web/usuarios/novo", data={"nome": "A", "email": "a@a.com"})
    client.post("/web/livros/novo", data={"titulo": "L1", "isbn": "111"})

    client.post("/emprestimos/", json={
        "usuario_id": 1,
        "livro_id": 1,
        "data_emprestimo": "2025-01-01",
        "data_devolucao_prevista": "2025-01-10"
    })

    # primeira devolução
    client.post("/web/emprestimos/1/devolver")

    # segunda devolução → deve ignorar, mas retornar 303/200
    r = client.post("/web/emprestimos/1/devolver")
    assert r.status_code in (200, HTTP_303_SEE_OTHER)

