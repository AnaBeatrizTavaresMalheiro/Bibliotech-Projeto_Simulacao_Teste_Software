# testes/fixtures/conftest_unit.py
import pytest
from datetime import date, timedelta

@pytest.fixture
def usuario_sem_multa():
    return {
        "id": 1,
        "nome": "Alice",
        "qtd_emprestimo": 0,
        "possui_multa_aberta": False
    }

@pytest.fixture
def usuario_com_multa():
    return {
        "id": 2,
        "nome": "Bob",
        "qtd_emprestimo": 1,
        "possui_multa_aberta": True
    }

@pytest.fixture
def livro_disponivel():
    return {
        "id": 10,
        "titulo": "Livro de Teste",
        "disponivel": True
    }

@pytest.fixture
def livro_indisponivel():
    return {
        "id": 11,
        "titulo": "Livro Ocupado",
        "disponivel": False
    }

@pytest.fixture
def datas():
    hoje = date.today()
    return {
        "data_emprestimo": hoje,
        "data_devolucao_prevista": hoje + timedelta(days=7),
        "data_devolucao_real_atrasada": hoje + timedelta(days=9),  # atraso de 2 dias
        "data_devolucao_real_no_prazo": hoje + timedelta(days=7)
    }


# Usuários
@pytest.fixture
def usuario_sem_multa():
    class Usuario:
        id = 1
        qtd_emprestimo = 0
        possui_multa_aberta = False
    return Usuario()

@pytest.fixture
def usuario_com_multa():
    class Usuario:
        id = 2
        qtd_emprestimo = 0
        possui_multa_aberta = True
    return Usuario()

@pytest.fixture
def usuario_com_limite():
    class Usuario:
        id = 3
        qtd_emprestimo = 3
        possui_multa_aberta = False
    return Usuario()

# Livros
@pytest.fixture
def livro_disponivel():
    class Livro:
        id = 10
        disponivel = True
    return Livro()

@pytest.fixture
def livro_indisponivel():
    class Livro:
        id = 11
        disponivel = False
    return Livro()

# Emprestimos
@pytest.fixture
def emprestimo_fake(usuario_sem_multa, livro_disponivel):
    class Emprestimo:
        usuario_id = usuario_sem_multa.id
        livro_id = livro_disponivel.id
        data_emprestimo = date.today()
        data_devolucao_prevista = date.today() + timedelta(days=7)
        data_devolucao_real = None
        dias_atraso = 0
        valor_multa = 0.0
    return Emprestimo()
