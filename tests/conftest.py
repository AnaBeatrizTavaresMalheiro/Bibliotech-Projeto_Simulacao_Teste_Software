# import pytest
# from datetime import date, timedelta

# @pytest.fixture
# def usuario_sem_multa():
#     return {"id": 1, "nome": "Luisa", "possui_multa_aberta": False, "qtd_emprestimo": 0}

# @pytest.fixture
# def usuario_com_multa():
#     return {"id": 2, "nome": "João", "possui_multa_aberta": True, "qtd_emprestimo": 1}

# @pytest.fixture
# def livro_disponivel():
#     return {"id": 1, "titulo": "Clean Code", "disponivel": True}

# @pytest.fixture
# def livro_indisponivel():
#     return {"id": 2, "titulo": "Design Patterns", "disponivel": False}

# @pytest.fixture
# def datas():
#     return {
#         "emprestimo": date.today(),
#         "prevista": date.today() + timedelta(days=7),
#         "devolucao_no_prazo": date.today() + timedelta(days=7),
#         "devolucao_atrasada": date.today() + timedelta(days=10),
#     }


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
# testes/fixtures/conftest.py
import pytest
from datetime import date, timedelta
from fastapi.testclient import TestClient
from src.server.main import app

@pytest.fixture
def client():
    return TestClient(app)

# Usuário sem multa
@pytest.fixture
def usuario_sem_multa():
    return {
        "id": 1,
        "nome": "Alice",
        "qtd_emprestimo": 0,
        "possui_multa_aberta": False
    }

# Usuário com multa
@pytest.fixture
def usuario_com_multa():
    return {
        "id": 2,
        "nome": "Bob",
        "qtd_emprestimo": 1,
        "possui_multa_aberta": True
    }

# Livro disponível
@pytest.fixture
def livro_disponivel():
    return {
        "id": 10,
        "titulo": "Livro de Teste",
        "disponivel": True
    }

# Livro indisponível
@pytest.fixture
def livro_indisponivel():
    return {
        "id": 11,
        "titulo": "Livro Ocupado",
        "disponivel": False
    }

# Datas de empréstimo/devolução
@pytest.fixture
def datas():
    hoje = date.today()
    return {
        "data_emprestimo": hoje,
        "data_devolucao_prevista": hoje + timedelta(days=7),
        "data_devolucao_real_atrasada": hoje + timedelta(days=9),  # atraso de 2 dias
        "data_devolucao_real_no_prazo": hoje + timedelta(days=7)
    }





@pytest.fixture
def usuario_com_multa(sessao):
    usuario = Usuario(id=2, nome="Bob", possui_multa_aberta=True, qtd_emprestimo=0)
    sessao.add(usuario)
    sessao.commit()
    yield usuario

@pytest.fixture
def livro_disponivel(sessao):
    livro = Livro(id=1, titulo="Livro Teste", disponivel=True)
    sessao.add(livro)
    sessao.commit()
    yield livro

